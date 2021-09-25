import RPi.GPIO as GPIO
from time import sleep


class GPIORPi:
    def __init__(self, mode=False) -> None:
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

    def read_pin(self, pin):
        self.GPIO.setup(pin, self.GPIO.IN)
        return GPIO.input(pin)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.GPIO.cleanup()


class MyGPIO(GPIO):
    def __init__(self, board_mode=GPIO.BCM, input_pins=[], output_pins=[]) -> None:
        super().__init__()
        self.setmode(board_mode)
        map(lambda pin: self.setup(int(pin), self.IN), input_pins)
        map(lambda pin: self.setup(int(pin), self.OUT), output_pins)

    def active_high_after_x_sec(self, pin, sec):
        self.output(pin, self.LOW)
        sleep(sec)
        self.output(pin, self.HIGH)

    def active_low_after_x_sec(self, pin, sec):
        self.output(pin, self.HIGH)
        sleep(sec)
        self.output(pin, self.LOW)

    def read_pin(self, pin):
        self.setup(pin, self.IN)
        return self.input(pin)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.cleanup()
