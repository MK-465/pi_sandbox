from abc import ABC, abstractmethod

from controller.lcd.display.lcd_display_command import LcdDisplayCommand


class LcdDisplayProvider(ABC):

    def __init__(self):
        self._lcd_display_command: LcdDisplayCommand = LcdDisplayCommand()

    @abstractmethod
    def lcd_display_command(self) -> LcdDisplayCommand:
        pass
