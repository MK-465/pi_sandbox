#!/usr/bin/env python
import time

import RPi.GPIO as GPIO
import pydevd_pycharm
import smbus

from controller.lcd.color.lcd_color_controller import LcdColorController
from controller.lcd.color.solid.lcd_solid_color_provider import LcdSolidColorProvider
from service.lcd_color_service import LcdColorService
from service.lcd_text_service import LcdTextService

DISPLAY_RGB_ADDR = 0x30
DISPLAY_TEXT_ADDR = 0x3e


def break_point():
    pydevd_pycharm.settrace('192.168.100.6', port=20888, stdoutToServer=True, stderrToServer=True)


class GroveRGBLCD:
    def __init__(self):
        self.rev = GPIO.RPI_REVISION
        self.bus = smbus.SMBus(1)

    def set_flash_color(self, flash_provider):
        flash_provider.set_flash_period(10)
        flash_provider.set_rgb(10, 50, 10)
        flash_provider.set_timer_pwm_1(100)
        flash_provider.set_rise_fall_time(5, 2)

    def setRGB(self, r, g, b):
        color_service: LcdColorService = LcdColorService(self.bus)
        color_service.set_flash_color(self.set_flash_color)
        color_service.set_solid_rgb_color(10, 50, 10)

        lcd_text_service: LcdTextService = LcdTextService(self.bus)
        # break_point()
        lcd_text_service.enable_two_lines()
        lcd_text_service.display_on_no_cursor()
        lcd_text_service.clear_row(0)
        lcd_text_service.clear_row(1)
        lcd_text_service.print_text_to_row(0, "Ho-ho :]")
        lcd_text_service.print_text_to_row(1, "R:%d; G:%d; B:%d" % (r, g, b))

    def setDefault(self):
        self.setRGB(5, 10, 10)
        time.sleep(2)
