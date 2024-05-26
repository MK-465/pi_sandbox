from abc import ABC

from controller.lcd.color.lcd_color_command import LcdColorCommand
from controller.lcd.color.lcd_color_state_provider import LcdColorStateProvider


class BasicLcdColorProvider(LcdColorStateProvider, ABC):

    def __init__(self):
        self._lcd_color_command: LcdColorCommand = LcdColorCommand()

    def set_rgb(self, red: int, green: int, blue: int):
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)
        pass

    def set_red(self, value: int):
        self._lcd_color_command.set_led1(value)
        return self

    def set_green(self, value: int):
        self._lcd_color_command.set_led2(value)
        return self

    def set_blue(self, value: int):
        self._lcd_color_command.set_led3(value)
        return self

    @property
    def lcd_color_command(self):
        return self._lcd_color_command
