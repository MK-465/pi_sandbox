from abc import ABC, abstractmethod

from controller.lcd.text.lcd_text_display_command import LcdTextDisplayCommand


class LcdTextDisplayProvider(ABC):

    @abstractmethod
    def lcd_display_command(self) -> LcdTextDisplayCommand:
        pass
