from enum import Enum

from controller.grove_command import GroveCommand


class LcdTextRegister(Enum):
    DISPLAY_SETUP_CONTROL = 0x80
    DISPLAY_TEXT_CONTROL = 0x40


class LcdDisplayCommand(GroveCommand):

    def __init__(self):
        super().__init__()

    def reset_values(self):
        self.clear_display()

    def set_display_state(self, value):
        self._registry_map[LcdTextRegister.DISPLAY_SETUP_CONTROL.value] = value

    def get_display_state(self):
        return self._registry_map[LcdTextRegister.DISPLAY_SETUP_CONTROL.value]

    def set_text_state(self, value):
        self._registry_map[LcdTextRegister.DISPLAY_TEXT_CONTROL.value] = value

    def get_text_state(self):
        return self._registry_map[LcdTextRegister.DISPLAY_TEXT_CONTROL.value]

    def clear_display(self):
        self.set_display_state(0x01)
