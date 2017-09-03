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

while True:
    # Wait for a connection
    print 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)

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
                            connection.sendall('1')
                        else:
                            connection.sendall('0')

            else:
                print 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()
