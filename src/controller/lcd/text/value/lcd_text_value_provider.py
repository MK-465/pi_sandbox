from abc import ABC

from controller.lcd.text.lcd_display_provider import LcdDisplayProvider


class LcdTextValueProvider(LcdDisplayProvider, ABC):

    def __init__(self):
        super().__init__()

    def write_char(self, char: str):
        self._lcd_display_command.set_text_state(ord(char))
