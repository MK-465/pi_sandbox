#!/usr/bin/env python
import time

import Adafruit_DHT
import RPi.GPIO as GPIO
import pydevd_pycharm
import smbus

from service.lcd_color_service import LcdColorService
from service.lcd_text_service import LcdTextService

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 3  # Change to the pin that you have connected the DHT11


# def break_point():
#     pydevd_pycharm.settrace('192.168.100.6', port=20888, stdoutToServer=True, stderrToServer=True)


def read_dht11():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN, 1, 10)
    if humidity is not None and temperature is not None:
        print("Temp={}*C  Humidity={}%".format(temperature, humidity))
        return temperature, humidity
    else:
        print("Failed to retrieve data from humidity sensor")
        return 0, 0


class GroveRGBLCD:
    def __init__(self):
        self.rev = GPIO.RPI_REVISION
        self.bus = smbus.SMBus(1)

    def set_flash_color(self, flash_provider):
        flash_provider.set_flash_period(10)
        flash_provider.set_rgb(10, 50, 10)
        flash_provider.set_timer_pwm_1(100)
        flash_provider.set_rise_fall_time(5, 2)

    def setRGB(self):
        # color_service: LcdColorService = LcdColorService(self.bus)
        # color_service.set_flash_color(self.set_flash_color)
        # color_service.set_solid_rgb_color(20, 5, 5)
        th = read_dht11()
        time.sleep(0.5)
        print("Temp={}*C".format(th[0]))
        # lcd_text_service: LcdTextService = LcdTextService(self.bus)
        # lcd_text_service.enable_two_lines()
        # lcd_text_service.display_on_no_cursor()
        # # for i in range(0, 5):
        #
        # lcd_text_service.clear_row(0)
        # lcd_text_service.clear_row(1)
        # lcd_text_service.print_text_to_row(0, "Temp={}*C".format(th[0]))
        # lcd_text_service.print_text_to_row(1, "Humidity={}%".format(th[1]))
        self.bus.close()
        # lcd_text_service.clear_row(0)
        # lcd_text_service.clear_row(1)
        # lcd_text_service.print_text_to_row(0, th[0])
        # lcd_text_service.print_text_to_row(1, th[1])
        # lcd_text_service.print_text_to_row(1, "R:%d; G:%d; B:%d" % (10, 50, 10))

        # color_service: LcdColorService = LcdColorService(self.bus)
        # color_service.set_flash_color(self.set_flash_color)
        # color_service.set_solid_rgb_color(30, 50, 50)
        #
        # lcd_text_service: LcdTextService = LcdTextService(self.bus)
        # # break_point()
        # lcd_text_service.enable_two_lines()
        # lcd_text_service.display_on_no_cursor()
        # lcd_text_service.clear_row(0)
        # lcd_text_service.clear_row(1)
        # lcd_text_service.print_text_to_row(0, "Ho-ho :]")
        # lcd_text_service.print_text_to_row(1, "R:%d; G:%d; B:%d" % (10, 50, 10))

        # read_dht11()

    def setDefault(self):
        self.setRGB()
        time.sleep(2)
