from abc import ABC, abstractmethod

from controller.lcd.lcd_color_command import LcdColorCommand


class LcdColorStateProvider(ABC):
    @abstractmethod
    def lcd_color_command(self) -> LcdColorCommand:
        pass
