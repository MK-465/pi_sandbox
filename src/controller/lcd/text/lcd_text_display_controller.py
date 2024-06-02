from controller.grove_controller import GroveController
from controller.lcd.text.lcd_text_display_command import LcdTextDisplayCommand


class LcdTextDisplayController(GroveController[LcdTextDisplayCommand]):

    def __init__(self, address: int, bus):
        super().__init__(address, bus)

    def to_default(self) -> None:
        self.process(LcdTextDisplayCommand())
        pass
