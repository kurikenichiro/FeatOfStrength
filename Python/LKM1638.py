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
        command_string = 'l'
        if color.lower() == 'green':
            command_string += 'g '
        elif color.lower() == 'red':
            command_string += 'r '
        else:
            command_string += 'n '

        command_string += str(position)
        command_string += '\n'
        print "Serial Write: ", command_string
        self.ser.write(command_string)

    def get_buttons(self):
        self.ser.write('b\n')
        read_string = self.ser.readline()
        if is_number(read_string):
            return int(read_string)
        else:
            return 0

    def set_time(self, dt, time_format):
        command_string = 'd '
        command_string += dt.strftime(time_format)
        command_string += '\n'
        self.ser.write(command_string)
