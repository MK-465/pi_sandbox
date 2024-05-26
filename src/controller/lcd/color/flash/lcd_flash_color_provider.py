from abc import ABC

from controller.lcd.color.basic_lcd_color_provider import BasicLcdColorProvider


class LcdFlashColorProvider(BasicLcdColorProvider, ABC):

    def __init__(self):
        super().__init__()
        self._lcd_color_command.set_channel_enable(int("101010", 2))

    def set_flash_period(self, period: int):
        self._lcd_color_command.set_flash_period(period)
        return self

    def set_timer_pwm_1(self, perc_of_flash: int):
        self._lcd_color_command.set_pwm1_timer(perc_of_flash)
        return self

    def set_rise_fall_time(self, time_to_rise: int, time_to_fall: int):
        assert 0 <= time_to_rise <= 15, "Time to rise must be between 0 and 15"
        assert 0 <= time_to_fall <= 15, "Time to fall must be between 0 and 15"
        # Combine the values into a single 8-bit value
        value = (time_to_fall << 4) | time_to_rise
        self._lcd_color_command.set_t_rise_fall(value)
        return self