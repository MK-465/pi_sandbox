from abc import ABC

from controller.lcd.color.basic_lcd_color_provider import BasicLcdColorProvider


class LcdSolidColorProvider(BasicLcdColorProvider, ABC):

    def __init__(self):
        super().__init__()
        self._lcd_color_command.set_channel_enable(int("010101", 2))
