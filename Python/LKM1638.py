from serial import Serial


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class LKM1638(object):
    """docstring for LKM1638"""

    def __init__(self, port):
        self.ser = Serial(port)
        print "Opened Serial Port: ", self.ser.name

    def set_led(self, color, position):
        commandString = 'l'
        if color.lower() == 'green':
            commandString += 'g '
        elif color.lower() == 'red':
            commandString += 'r '
        else:
            commandString += 'n '

        commandString += str(position)
        commandString += '\n'
        print "Serial Write: ", commandString
        self.ser.write(commandString)

    def get_buttons(self):
        self.ser.write('b\n')
        readString = self.ser.readline()
        if is_number(readString):
            return int(readString)
        else:
            return 0

    def set_time(self, dt, timeFormat):
        commandString = 'd '
        commandString += dt.strftime(timeFormat)
        commandString += '\n'
        self.ser.write(commandString)
