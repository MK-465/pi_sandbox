from abc import ABC

from controller.lcd.text.lcd_text_display_command import LcdTextDisplayCommand
from controller.lcd.text.lcd_text_display_provider import LcdTextDisplayProvider


class LcdTextStateProvider(LcdTextDisplayProvider, ABC):

    def __init__(self):
        super().__init__()
        self._lcd_display_command: LcdTextDisplayCommand = LcdTextDisplayCommand()

    @property
    def lcd_display_command(self) -> LcdTextDisplayCommand:
        return self._lcd_display_command

    def clear_display(self):
        self._lcd_display_command.set_display_state(0x01)

    def return_home(self):
        self._lcd_display_command.set_display_state(0x02)

    def display_off(self):
        self._lcd_display_command.set_display_state(0x08)

    def display_on_no_cursor(self):
        self._lcd_display_command.set_display_state(0x08 | 0x04)

    def enable_two_lines(self):
        self._lcd_display_command.set_display_state(0x28)

    def decrement_cursor(self):
        self._lcd_display_command.set_display_state(0x04)

    def increment_cursor(self):
        self._lcd_display_command.set_display_state(0x06)

    def shift_display_right(self):
        self._lcd_display_command.set_display_state(0x05)

    def shift_display_left(self):
        self._lcd_display_command.set_display_state(0x07)

    def display_off_cursor_off(self):
        self._lcd_display_command.set_display_state(0x08)

    def display_off_cursor_on(self):
        self._lcd_display_command.set_display_state(0x0A)

    def display_on_cursor_off(self):
        self._lcd_display_command.set_display_state(0x0C)

    def display_on_cursor_blinking(self):
        self._lcd_display_command.set_display_state(0x0E)

    def shift_cursor_position_left(self):
        self._lcd_display_command.set_display_state(0x10)

    def shift_cursor_position_right(self):
        self._lcd_display_command.set_display_state(0x14)

    def shift_entire_display_left(self):
        self._lcd_display_command.set_display_state(0x18)

    def shift_entire_display_right(self):
        self._lcd_display_command.set_display_state(0x1C)

    def force_cursor_to_beginning_first_line(self):
        self._lcd_display_command.set_display_state(0x80)

    def force_cursor_to_beginning_second_line(self):
        self._lcd_display_command.set_display_state(0xC0)
