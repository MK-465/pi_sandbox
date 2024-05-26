from abc import ABC

from controller.lcd.lcd_color_command import LcdColorCommand
from controller.lcd.lcd_color_state_provider import LcdColorStateProvider


class LcdSolidColorProvider(LcdColorStateProvider, ABC):

    def __init__(self):
        self._lcd_color_command: LcdColorCommand = LcdColorCommand()
        self._lcd_color_command.set_channel_enable(int("010101", 2))

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

# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x0, int("00000000", 2))
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x1, int("00001000", 2))
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x2, 100)
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x3, zeroreset)
#
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x4, int("101010", 2))
# # self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x4, 0)
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x5, int("10001000", 2))
#
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x6, 10)
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x7, 50)
# self.bus.write_byte_data(DISPLAY_RGB_ADDR, 0x8, 50)
