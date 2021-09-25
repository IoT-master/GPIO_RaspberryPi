import RPi.GPIO as GPIO
from time import sleep


class MyGPIO:
    def __init__(self, board_mode=GPIO.BCM, input_pins=[], output_pins=[]):
        GPIO.setmode(board_mode)
        list(map(lambda pin: GPIO.setup(int(pin), GPIO.IN), input_pins))
        list(map(lambda pin: GPIO.setup(int(pin), GPIO.OUT), output_pins))

    def output_latch_down(self, pin, seconds):
        GPIO.output(pin, GPIO.LOW)
        sleep(seconds)
        GPIO.output(pin, GPIO.HIGH)

    def output_latch_up(self, pin, seconds):
        GPIO.output(pin, GPIO.HIGH)
        sleep(seconds)
        GPIO.output(pin, GPIO.LOW)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        GPIO.cleanup()
