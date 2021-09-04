#!/usr/bin/python3
from GPIORPi import GPIORPi

seconds = .15
with GPIORPi(mode=False) as rpi:
    for each_io in [14, 15, 17, 18]:
        rpi.output_latch_down(each_io, seconds)

