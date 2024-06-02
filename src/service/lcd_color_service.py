from typing import Callable

from controller.lcd.color.flash.lcd_flash_color_provider import LcdFlashColorProvider
from controller.lcd.color.lcd_color_controller import LcdColorController
from controller.lcd.color.solid.lcd_solid_color_provider import LcdSolidColorProvider

DISPLAY_RGB_ADDR = 0x30


class LcdColorService:

    def __init__(self, bus):
        self.bus = bus
        self.color_controller = LcdColorController(DISPLAY_RGB_ADDR, self.bus)

    def _set_solid_color(self, state: Callable[[LcdSolidColorProvider], None]):
        provider_solid_state: LcdSolidColorProvider = LcdSolidColorProvider()
        state(provider_solid_state)
        self.color_controller.process(provider_solid_state.lcd_color_command)

    def set_solid_rgb_color(self, r: int, g: int, b: int):
        self._set_solid_color(lambda solid_state: solid_state.set_rgb(r, g, b))

    def set_flash_color(self, state: Callable[[LcdFlashColorProvider], None]):
        provider_flash_state: LcdFlashColorProvider = LcdFlashColorProvider()
        state(provider_flash_state)
        self.color_controller.process(provider_flash_state.lcd_color_command)
