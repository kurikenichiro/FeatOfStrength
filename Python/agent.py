from datetime import datetime
from datetime import timedelta
from LKM1638 import LKM1638
import select
import socket
from stringhelper import is_number

# serial port
port = '/dev/cu.usbmodem3208451'

# time variables
current_dt = datetime.now()
delta = timedelta(microseconds=100000)

module = LKM1638(port)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print 'starting up on %s port %s' % server_address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

read_list = [server_socket]

while True:
    # Time and Button Action Loop
    dt = datetime.now()
    utc_dt = datetime.utcnow()

    time_diff = dt - current_dt

    if time_diff > delta:
        current_dt = dt
        # print "Current Time: ", str(dt)
        # print "Current UTC Time: ", str(utc_dt)

        # Display Time based on button states
        buttons = module.get_buttons()
        if buttons & 0x01:
            time_format = '%m%d%H%M'
        else:
            time_format = '%m%d%I%M'

        if buttons & 0x02:
            module.set_time(utc_dt, time_format)
        else:
            module.set_time(dt, time_format)

    # Socket Loop
    readable, writable, errored = select.select(read_list, [], [], 0.1)

    for s in readable:
        if s is server_socket:
            client_socket, client_address = server_socket.accept()
            read_list.append(client_socket)
            print "connection from", client_address
        else:
            try:
                # receive commands and process it
                while True:
                    data = s.recv(16)

                    if data:
                        print 'received "%s"' % data
                        data = data.strip()
                        command = data.split(' ')

                        if command[0] == 'led' and len(command) == 3:
                            color = command[1]
                            if is_number(command[2]):
                                position = int(command[2])
                                module.set_led(color, position)
                                print 'Led: ', position, ' ', color
                        elif command[0] == 'button' and len(command) == 2:
                            if is_number(command[1]):
                                button = int(command[1])
                                # Poll button and get state
                                module.get_buttons()
                                state = module.get_buttons() & (0x01 << button)
                                print 'Button: ', button, ' ', state
                                if state:
                                    s.sendall('1')
                                else:
                                    s.sendall('0')

                    else:
                        print 'no more data from', client_address
                        break

            finally:
                # Clean up the connection
                s.close()
                read_list.remove(s)
