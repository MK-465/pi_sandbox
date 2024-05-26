from abc import ABC

from controller.grove_controller import GroveController
from controller.lcd.color.lcd_color_command import LcdColorCommand


class LcdColorController(GroveController[LcdColorCommand], ABC):

    def __init__(self, address: int, bus):
        super().__init__(address, bus)



