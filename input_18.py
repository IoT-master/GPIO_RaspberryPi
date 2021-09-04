#!/usr/bin/python3
from GPIORPi import GPIORPi
from time import sleep
seconds = .15
with GPIORPi(mode=False) as rpi:
    while True:
        if rpi.input(18):
            print("yes")
        sleep(2)
