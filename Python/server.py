import select
import socket
from stringhelper import is_number

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

read_list = [sock]

while True:
    # Wait for a connection
    print 'waiting for a connection'
    readable, writable, errored = select.select(read_list, [], [], 0.1)

    for s in readable:
        if s is sock:
            client_socket, client_address = sock.accept()
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
                                print 'Led: ', position, ' ', color
                        elif command[0] == 'button' and len(command) == 2:
                            if is_number(command[1]):
                                button = int(command[1])
                                # Poll button and get state
                                state = True
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
