import RPi.GPIO as GPIO
from time import sleep
class GPIORPi:
    def __init__(self, mode=True) -> None:
        self.GPIO = GPIO
        if mode:
            self.GPIO.setmode(GPIO.BOARD)
        else:
            self.GPIO.setmode(GPIO.BCM)
    
    def output_latch_down(self, pin, seconds):
        self.GPIO.setup(pin, self.GPIO.OUT)
        self.GPIO.output(pin, self.GPIO.LOW)
        sleep(seconds)
        self.GPIO.output(pin, self.GPIO.HIGH)

    def output_latch_up(self, pin, seconds):
        self.GPIO.setup(pin, self.GPIO.OUT)
        self.GPIO.output(pin, self.GPIO.HIGH)
        sleep(seconds)
        self.GPIO.output(pin, self.GPIO.LOW)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.GPIO.cleanup()
        