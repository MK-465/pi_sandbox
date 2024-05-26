from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from controller.grove_command import GroveCommand

T = TypeVar('T', bound=GroveCommand)


class GroveController(Generic[T], ABC):

    def __init__(self, address: int, bus):
        self.address = address
        self.bus = bus

    @property
    def get_address(self):
        return self.address

    def process(self, command: T) -> None:
        registry_map = command.registry_map
        for key, value in registry_map.items():
            self.bus.write_byte_data(self.address, key, value)
        pass

    @abstractmethod
    def to_default(self) -> None:
        pass
