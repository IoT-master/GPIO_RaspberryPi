from GPIORPi import MyGPIO
from time import sleep

with MyGPIO(input_pins=[26]) as motion_dectector:
    while True:
        if motion_dectector.read_pin(26):
            print(True)
        else:
            print(False)
        sleep(0.1)
