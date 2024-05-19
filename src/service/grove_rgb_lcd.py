#!/usr/bin/env python
import random
import sys
import time
import smbus
import RPi.GPIO as GPIO
import pydevd_pycharm

DISPLAY_RGB_ADDR = 0x30
DISPLAY_TEXT_ADDR = 0x3e


class GroveRGBLCD:
    def __init__(self):
        self.rev = GPIO.RPI_REVISION
        self.bus = smbus.SMBus(1)

    # this device has two I2C addresses

    # set backlight to (R,G,B) (values from 0..255 for each)
    def setRGB(self, r, g, b):
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0, 0)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 1, 0)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xaa)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 4, r)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 3, g)
        self.bus.write_byte_data(DISPLAY_RGB_ADDR, 2, b)

    def textCommand(self, cmd):
        self.bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, cmd)

    # set display text \n for second line(or auto wrap)
    def setText(self, text):
        self.textCommand(0x01)  # clear display
        self.textCommand(0x08 | 0x04)  # display on, no cursor
        self.textCommand(0x28)  # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))

    # Update the display without erasing the display
    def setText_norefresh(self, text):
        self.textCommand(0x02)  # return home
        time.sleep(.05)
        self.textCommand(0x08 | 0x04)  # display on, no cursor
        self.textCommand(0x28)  # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        while len(text) < 32:  # clears the rest of the screen
            text += ' '
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))

    # Create a custom character (from array of row patterns)
    def create_char(self, location, pattern):
        """
        Writes a bit pattern to LCD CGRAM

        Arguments:
        location -- integer, one of 8 slots (0-7)
        pattern -- byte array containing the bit pattern, like as found at
               https://omerk.github.io/lcdchargen/
        """
        location &= 0x07  # Make sure location is 0-7
        self.textCommand(0x40 | (location << 3))
        self.bus.write_i2c_block_data(DISPLAY_TEXT_ADDR, 0x40, pattern)

    def setDefault(self):
        pydevd_pycharm.settrace('192.168.100.6', port=20888, stdoutToServer=True, stderrToServer=True)

        try:
            self.setRGB(0, 255, 0)

            self.setText("Grove - LCD RGB Backlight")
            time.sleep(2)

            # self.setText("Hello World")
            # time.sleep(2)

            # self.setText("Random colors")
            # for i in range(0, 51):
            #     self.setRGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            #     time.sleep(.1)
            # time.sleep(1)
            #
            # # ascii char 255 is the cursor character
            # self.setRGB(255, 255, 255)
            # self.setText(chr(255) * 32)
            # time.sleep(2)
            #
            # # typewriter
            # self.setRGB(255, 127, 0)
            # str = "Hello World"
            # for i in range(0, 12):
            #     self.setText(str[:i])
            #     time.sleep(.2)
            # time.sleep(2)
            #
            # self.setRGB(255, 0, 255)
            # self.setText("1234567890ABCDEF1234567890ABCDEF")
            # time.sleep(2)
            #
            # self.setText("Long strings will be truncated at 32 chars")
            # time.sleep(2)
            #
            # self.setRGB(0, 255, 0)
            # self.setText("Automatic word wrapping")
            # time.sleep(2)
            #
            # self.setText("Manual\nword wrapping")
            # time.sleep(2)
            #
            # self.setRGB(0, 255, 255)
            # self.setText("ASCII printable and extended")
            # time.sleep(2)
            #
            # chars = ""
            # for a in range(32, 256):
            #     chars += chr(a)
            #     if len(chars) == 32:
            #         self.setText(chars)
            #         chars = ""
            #         time.sleep(2)

            # self.setRGB(0, 255, 0)
            # self.setText("Solid colors")
            # time.sleep(2)
            #
            # self.setText("Red")
            # self.setRGB(255, 0, 0)
            # time.sleep(.5)
            #
            # self.setText("Green")
            # self.setRGB(0, 255, 0)
            # time.sleep(.5)
            #
            # self.setText("Blue")
            # self.setRGB(0, 0, 255)
            # time.sleep(.5)
            #
            # self.setText("Yellow")
            # self.setRGB(255, 255, 0)
            # time.sleep(.5)
            #
            # self.setText("Magenta")
            # self.setRGB(255, 0, 255)
            # time.sleep(.5)
            #
            # self.setText("Cyan")
            # self.setRGB(0, 255, 255)
            # time.sleep(.5)
            #
            # self.setText("White")
            # self.setRGB(255, 255, 255)
            # time.sleep(.5)
            #
            # self.setText("Black")
            # self.setRGB(0, 0, 0)
            # time.sleep(.5)

            self.setText("Grey")
            self.setRGB(127, 127, 127)
            # time.sleep(.5)

            # self.setRGB(255, 255, 255)
            # self.setText("Alphanumeric characters")
            # time.sleep(2)
            #
            # self.setText("1234567890ABCDEF1234567890ABCDEF")
            # time.sleep(2)
            #
            # self.setText("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            # time.sleep(2)
            #
            # self.setText("abcdefghijklmnopqrstuvwxyz")
            # time.sleep(2)
            #
            # self.setText("1234567890")
            # time.sleep(2)
            #
            # self.setText("Shades of red")
            # for c in range(0, 255):
            #     self.setRGB(255, 255 - c, 255 - c)
            #     time.sleep(.01)
            #
            # self.setText("Shades of green")
            # for c in range(0, 255):
            #     self.setRGB(255 - c, 255, 255 - c)
            #     time.sleep(.01)
            #
            # self.setText("Shades of blue")
            # for c in range(0, 255):
            #     self.setRGB(255 - c, 255 - c, 255)
            #     time.sleep(.01)
            #
            # self.setText("Shades of yellow")
            # for c in range(0, 255):
            #     self.setRGB(255, 255, 255 - c)
            #     time.sleep(.01)
            #
            # self.setText("Shades of magenta")
            # for c in range(0, 255):
            #     self.setRGB(255, 255 - c, 255)
            #     time.sleep(.01)
            #
            # self.setText("Shades of cyan")
            # for c in range(0, 255):
            #     self.setRGB(255 - c, 255, 255)
            #     time.sleep(.01)

            # self.setText("Shades of grey")
            # for c in range(0, 255):
            #     self.setRGB(c, c, c)
            #     time.sleep(.01)

        except KeyboardInterrupt:
            self.setText("KeyboardInterrupt")
            self.setRGB(255, 0, 0)
        except IOError:
            self.setText("IOError")
            self.setRGB(255, 0, 0)

        time.sleep(1)
        self.setText("All done")
        self.setRGB(0, 255, 0)
        #
        # self.setText("Hi \n This is an LCD test")
        # self.setRGB(10, 128, 64)
        # time.sleep(2)
        # # for c in range(0, 255):
        # #     self.setText_norefresh("Going to sleep in {}...".format(str(c)))
        # #     self.setRGB(c, 255 - c, 0)
        # #     time.sleep(0.1)
        # self.setRGB(0, 255, 0)
        # self.setText("Bye bye, this should wrap onto next line")


