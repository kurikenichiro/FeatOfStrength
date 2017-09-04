import socket
import argparse
from stringhelper import is_number

parser = argparse.ArgumentParser()
parser.add_argument("cmd",
                    help="command to send, ex: 'led green 0', 'button 6'",
                    type=str)
args = parser.parse_args()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)

# print 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    message = args.cmd
    # print 'sending "%s"' % message
    sock.sendall(message)

    message = message.strip()
    command = message.split(' ')

    if command[0] == 'button' and is_number(command[1]) and len(command) == 2:
        data = sock.recv(1)
        print 'button: %s, state: %s' % (command[1], data)

finally:
    # print 'closing socket'
    sock.close()
