import time
from abc import abstractmethod, ABC
from typing import TypeVar, Generic

import pydevd_pycharm
import smbus

from controller.grove_command import GroveCommand

T = TypeVar('T', bound=GroveCommand)

# def break_point():
#     pydevd_pycharm.settrace('192.168.100.6', port=20888, stdoutToServer=True, stderrToServer=True)


class GroveController(Generic[T], ABC):

    def __init__(self, address: int, bus):
        self.address = address
        self.bus = bus

    @property
    def get_address(self):
        return self.address

    def process(self, command: T) -> None:
        max_attempts = 10
        for attempt in range(max_attempts):
            try:
                # self.bus = smbus.SMBus(1)
                registry_map = command.registry_map
                for key, value in registry_map.items():
                    self.bus.write_byte_data(self.address, key, value)
                # self.bus.close()
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")
                time.sleep(0.3)
        else:
            print(f"All {max_attempts} attempts failed.")

    @abstractmethod
    def to_default(self) -> None:
        pass
