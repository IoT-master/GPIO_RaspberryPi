#!/usr/bin/python3
from GPIORPi import MyGPIO

seconds = 0.15
with MyGPIO(input_pins=[14, 15, 17, 18]) as rpi:
    for each_io in [14, 15, 17, 18]:
        rpi.output_latch_down(each_io, seconds)
