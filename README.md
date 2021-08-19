GPIO is your standard pins that can be used to turn devices on and off. For example, a LED.
I2C (Inter-Integrated Circuit) pins allow you to connect and talk to hardware modules that support this protocol (I2C Protocol). This protocol will typically take up two pins.
SPI (Serial Peripheral Interface Bus) pins can be used to connect and talk to SPI devices. Pretty much the same as I2C but makes use of a different protocol.
UART (Universal asynchronous receiver/transmitter) is the serial pins used to communicate with other devices.
DNC stands for do not connect, this is pretty self-explanatory.
The power pins pull power directly from the Raspberry Pi.
GND are the pins you use to ground your devices. It doesn’t matter which pin you use as they are all connected to the same line.

GPIO board (GPIO.Board) references the physical numbering of the pins. For example, the top left pin is 1, and the top right pin 2. It continues to count upwards as you go from top to bottom until you run out of pins. In our diagram, you can see this numbering in the middle of each group.

GPIO BCM (GPIO.BCM) is the Broadcom Soc Channel numbering. In the diagram above, you can find the number after GPIO. For example on the Raspberry Pi 3, the pin below 3v3 is GPIO2, so the number for this pin is 2 in BCM mode.

The operating voltage of the GPIO pins is 3.3v with a maximum current draw of 16mA

The 5v pins give direct access to the 5v supply coming from your mains adaptor, less power than used by the Raspberry Pi itself. A Pi can be powered directly from these pins, and it can also power other 5v devices. When using these pins directly, be careful and check your voltages before making a connection because they bypass any safety features, such as the voltage regulator and fuse which are there to protect your Pi. Bypass these with a higher voltage and you could render your Pi inoperable.

By connecting the long leg of the LED, the anode to the 3.3v pin via a resistor, and the shorter leg, the cathode to any of the Ground (gnd) pins we can check that our LED lights up and is working

Credit from:
https://pimylifeup.com/raspberry-pi-gpio/
https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html
