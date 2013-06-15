import time
import serial
import threading
import json

class Arduino():
    def __init__(self, serial_port, serial_baud):
        self.serial_port = serial_port
        self.serial_baud = serial_baud
        self.serial = serial.Serial(serial_port, serial_baud)
        self.listener = self.Listener(self.serial)
        self.listener.start()
        self.current_state = None

    class Listener(threading.Thread):
        def __init__(self, ard):
            self.arduino = ard
            self.running = True
            self.state = {}
            self.callbacks = []
            threading.Thread.__init__(self)

        def run(self):
            while self.running:
                try:
                    self.arduino.flushInput()
                    arduinoCommand = self.arduino.readline().rstrip()
                    self.state = json.loads(arduinoCommand)
                    for callback in self.callbacks:
                        callback(self.state)
                except Exception as e:
                    pass

    def send_command(self, command):
        self.serial.write(command)
        time.sleep(1)

    def create_pin_string(self, pins):
        if not isinstance(pins, list):
            pins = [pins]
        pins = [str(x) for x in pins]
        return "#" + ','.join(pins) + ";"

    def set_low(self, pins, value):
        self.set_pwm(pins, 0)

    def set_high(self, pins, value):
        self.set_pwm(pins, 255)

    def set_pwm(self, pins, value):
        command = self.create_pin_string(pins)
        command += "p"
        value = int(value)
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        command += str(value)
        self.send_command(command)

    def set_pin_mode(self, pins, mode, ensure=False):
        command = self.create_pin_string(pins)
        command += "m"
        if mode.lower() == "input":
            command += 'i'
        elif mode.lower() == "output":
            command += 'o'
        elif mode.lower() == "lcd":
            mode = "output"
            command += 'l'
        else:
            pass
        if ensure:
            done = False
            if not isinstance(pins, list):
                pins = [pins]
            pins = [str(x) for x in pins]
            while not done:
                self.send_command(command)
                self.send_command("?")
                self.current_state = self.listener.state
                done = True
                for pin in pins:
                    if done:
                        done = self.current_state[pin] == mode
        else:
            self.send_command(command)
