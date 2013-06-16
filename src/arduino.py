import serial
import time


class Arduino():
    def __init__(self, serial_port, serial_baud):
        self.serial_port = serial_port
        self.serial_baud = serial_baud
        self.serial = serial.Serial(serial_port, serial_baud)

    def change_color(self, x, y, r, g, b):
        r = int(r/7)
        g = int(g/7)
        b = int(b/7)

        command = ""
        command += chr(x)
        command += chr(y)
        command += chr(r)
        command += chr(g)
        command += chr(b)
        self.serial.write(command)

    def show(self, x):
        command = chr(x)
        command += chr(255)
        self.serial.write(command)
