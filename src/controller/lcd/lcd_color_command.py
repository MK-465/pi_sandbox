from enum import Enum

from controller.grove_command import GroveCommand


class LcdColorRegister(Enum):
    RESET_CONTROL = 0
    FLASH_PERIOD = 1
    PWM1_TIMER = 2
    PWM2_TIMER = 3
    CHANNEL_ENABLE = 4
    T_RISE_FALL = 5
    LED1 = 6
    LED2 = 7
    LED3 = 8


class LcdColorCommand(GroveCommand):

    def __init__(self):
        super().__init__()
        self.reset_values()

    def reset_values(self):
        self.set_control(0x00)
        self.set_flash_period(0x00)
        self.set_pwm1_timer(0x01)
        self.set_pwm2_timer(0x01)
        self.set_channel_enable(0x00)
        self.set_t_rise_fall(0x00)
        self.set_led1(0x4F)
        self.set_led2(0x4F)
        self.set_led3(0x4F)

    def get_control(self):
        return self._registry_map[LcdColorRegister.RESET_CONTROL.value]

    def set_control(self, value):
        self._registry_map[LcdColorRegister.RESET_CONTROL.value] = value

    def get_flash_period(self):
        return self._registry_map[LcdColorRegister.FLASH_PERIOD.value]

    def set_flash_period(self, value):
        self._registry_map[LcdColorRegister.FLASH_PERIOD.value] = value

    def get_pwm1_timer(self):
        return self._registry_map[LcdColorRegister.PWM1_TIMER.value]

    def set_pwm1_timer(self, value):
        self._registry_map[LcdColorRegister.PWM1_TIMER.value] = value

    def get_pwm2_timer(self):
        return self._registry_map[LcdColorRegister.PWM2_TIMER.value]

    def set_pwm2_timer(self, value):
        self._registry_map[LcdColorRegister.PWM2_TIMER.value] = value

    def get_channel_enable(self):
        return self._registry_map[LcdColorRegister.CHANNEL_ENABLE.value]

    def set_channel_enable(self, value):
        self._registry_map[LcdColorRegister.CHANNEL_ENABLE.value] = value

    def get_t_rise_fall(self):
        return self._registry_map[LcdColorRegister.T_RISE_FALL.value]

    def set_t_rise_fall(self, value):
        self._registry_map[LcdColorRegister.T_RISE_FALL.value] = value

    def get_led1(self):
        return self._registry_map[LcdColorRegister.LED1.value]

    def set_led1(self, value):
        self._registry_map[LcdColorRegister.LED1.value] = value

    def get_led2(self):
        return self._registry_map[LcdColorRegister.LED2.value]

    def set_led2(self, value):
        self._registry_map[LcdColorRegister.LED2.value] = value

    def get_led3(self):
        return self._registry_map[LcdColorRegister.LED3.value]

    def set_led3(self, value):
        self._registry_map[LcdColorRegister.LED3.value] = value

    def __str__(self):
        return f"Control: {self.get_control()}, Flash Period: {self.get_flash_period()}, PWM1 Timer: {self.get_pwm1_timer()}, PWM2 Timer: {self.get_pwm2_timer()}, Channel Enable: {self.get_channel_enable()}, T Rise Fall: {self.get_t_rise_fall()}, LED1: {self.get_led1()}, LED2: {self.get_led2()}, LED3: {self.get_led3()}"
