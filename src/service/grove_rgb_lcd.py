#!/usr/bin/env python
import time

import RPi.GPIO as GPIO
import smbus

from controller.lcd.color.flash.lcd_flash_color_provider import LcdFlashColorProvider
from controller.lcd.color.lcd_color_controller import LcdColorController
from controller.lcd.color.solid.lcd_solid_color_provider import LcdSolidColorProvider

DISPLAY_RGB_ADDR = 0x30
DISPLAY_TEXT_ADDR = 0x3e


# def break_point():
#     pydevd_pycharm.settrace('192.168.100.6', port=20888, stdoutToServer=True, stderrToServer=True)


class GroveRGBLCD:
    def __init__(self):
        self.rev = GPIO.RPI_REVISION
        self.bus = smbus.SMBus(1)

    def setRGB(self, r, g, b):
        provider: LcdFlashColorProvider = LcdFlashColorProvider()
        provider.set_rgb(r, g, b)
        provider.set_flash_period(30)
        provider.set_timer_pwm_1(50)
        provider.set_rise_fall_time(15, 15)
        color_controller: LcdColorController = LcdColorController(DISPLAY_RGB_ADDR, self.bus)
        color_controller.process(provider.lcd_color_command)

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
        # break_point()
        self.setText_norefresh("The rise of the sun :]")
        # self.setText_norefresh("KeyboardInterrupt")
        self.setRGB(5, 5, 30)
        time.sleep(2)
