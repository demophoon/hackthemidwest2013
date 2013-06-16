import serial
import time


class Arduino():
    def __init__(self, serial_port, serial_baud):
        self.serial_port = serial_port
        self.serial_baud = serial_baud
        self.serial = serial.Serial(serial_port, serial_baud)

    def change_color(self, x, y, r, g, b):
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

def testCase():
    a = Arduino("COM6", 9600)
    for x in range(22):
        for y in range(20):
            a.change_color(x,y,50,50,50)
            time.sleep(.1)
    return a
