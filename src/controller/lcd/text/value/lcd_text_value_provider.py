from abc import ABC

from controller.lcd.text.lcd_text_display_command import LcdTextDisplayCommand
from controller.lcd.text.lcd_text_display_provider import LcdTextDisplayProvider


class LcdTextValueProvider(LcdTextDisplayProvider, ABC):

    def __init__(self):
        self._lcd_display_command: LcdTextDisplayCommand = LcdTextDisplayCommand()

    @property
    def lcd_display_command(self) -> LcdTextDisplayCommand:
        return self._lcd_display_command

    def write_char(self, char: str):
        self._lcd_display_command.set_text_state(ord(char))
