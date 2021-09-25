import RPi.GPIO as GPIO
from time import sleep


class MyGPIO:
    def __init__(self, board_mode=GPIO.BCM, input_pins=[], output_pins=[]) -> None:
        self.GPIO = GPIO
        self.GPIO.setmode(board_mode)
        list(map(lambda pin: self.GPIO.setup(int(pin), self.GPIO.IN), input_pins))
        list(map(lambda pin: self.GPIO.setup(int(pin), self.GPIO.OUT), output_pins))

    def output_latch_down(self, pin, seconds):
        self.GPIO.output(pin, self.GPIO.LOW)
        sleep(seconds)
        self.GPIO.output(pin, self.GPIO.HIGH)

    def output_latch_up(self, pin, seconds):
        self.GPIO.output(pin, self.GPIO.HIGH)
        sleep(seconds)
        self.GPIO.output(pin, self.GPIO.LOW)

    def read_pin(self, pin):
        return self.GPIO.input(pin)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.GPIO.cleanup()
