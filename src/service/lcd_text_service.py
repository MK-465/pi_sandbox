from typing import Callable

from controller.lcd.text.lcd_text_display_controller import LcdTextDisplayController
from controller.lcd.text.state.lcd_text_state_provider import LcdTextStateProvider
from controller.lcd.text.value.lcd_text_value_provider import LcdTextValueProvider

DISPLAY_TEXT_ADDR = 0x3e


class LcdTextService:

    def __init__(self, bus):
        self.bus = bus
        self.text_controller = LcdTextDisplayController(DISPLAY_TEXT_ADDR, self.bus)

    def set_test_state(self, state: Callable[[LcdTextStateProvider], None]):
        provider_text_state: LcdTextStateProvider = LcdTextStateProvider()
        state(provider_text_state)
        self.text_controller.process(provider_text_state.lcd_display_command)

    def _set_test_char(self, char: str):
        provider_text_value: LcdTextValueProvider = LcdTextValueProvider()
        provider_text_value.write_char(char)
        self.text_controller.process(provider_text_value.lcd_display_command)

    def print_text_to_row(self, row, text):
        trimmed_text = text[:16]
        self.move_cursor_to_row(row)
        for c in trimmed_text:
            self._set_test_char(c)

    def clear_row(self, row):
        self.print_text_to_row(row, self.generate_equal_chars(' ', 16))

    @staticmethod
    def generate_equal_chars(char: str, length: int) -> str:
        return char * length

    def move_cursor_to_row(self, row):
        if row == 0:
            self.force_cursor_to_beginning_first_line()
        else:
            self.force_cursor_to_beginning_second_line()

    def clear_display(self):
        self.set_test_state(lambda text_state: text_state.clear_display())

    def return_home(self):
        self.set_test_state(lambda text_state: text_state.return_home())

    def display_off(self):
        self.set_test_state(lambda text_state: text_state.display_off())

    def display_on_no_cursor(self):
        self.set_test_state(lambda text_state: text_state.display_on_no_cursor())

    def enable_two_lines(self):
        self.set_test_state(lambda text_state: text_state.enable_two_lines())

    def decrement_cursor(self):
        self.set_test_state(lambda text_state: text_state.decrement_cursor())

    def increment_cursor(self):
        self.set_test_state(lambda text_state: text_state.increment_cursor())

    def shift_display_right(self):
        self.set_test_state(lambda text_state: text_state.shift_display_right())

    def shift_display_left(self):
        self.set_test_state(lambda text_state: text_state.shift_display_left())

    def display_off_cursor_off(self):
        self.set_test_state(lambda text_state: text_state.display_off_cursor_off())

    def display_off_cursor_on(self):
        self.set_test_state(lambda text_state: text_state.display_off_cursor_on())

    def display_on_cursor_off(self):
        self.set_test_state(lambda text_state: text_state.display_on_cursor_off())

    def display_on_cursor_blinking(self):
        self.set_test_state(lambda text_state: text_state.display_on_cursor_blinking())

    def shift_cursor_position_left(self):
        self.set_test_state(lambda text_state: text_state.shift_cursor_position_left())

    def shift_cursor_position_right(self):
        self.set_test_state(lambda text_state: text_state.shift_cursor_position_right())

    def shift_entire_display_left(self):
        self.set_test_state(lambda text_state: text_state.shift_entire_display_left())

    def shift_entire_display_right(self):
        self.set_test_state(lambda text_state: text_state.shift_entire_display_right())

    def force_cursor_to_beginning_first_line(self):
        self.set_test_state(lambda text_state: text_state.force_cursor_to_beginning_first_line())

    def force_cursor_to_beginning_second_line(self):
        self.set_test_state(lambda text_state: text_state.force_cursor_to_beginning_second_line())
