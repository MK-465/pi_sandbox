from abc import ABC

from controller.lcd.display.lcd_display_provider import LcdDisplayProvider


class LcdDisplayStateProvider(LcdDisplayProvider, ABC):

    def __init__(self):
        super().__init__()

    def clear_display(self):
        self._lcd_display_command.set_display_state(0x01)

    def return_home(self):
        self._lcd_display_command.set_display_state(0x02)

