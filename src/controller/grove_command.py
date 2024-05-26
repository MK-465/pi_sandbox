from typing import Dict


class GroveCommand:
    def __init__(self):
        self._registry_map: Dict[int, int] = {}

    @property
    def registry_map(self):
        return self._registry_map

    def get_register_value(self, register: int):
        return self._registry_map[register]

    def set_register_value(self, register: int, value: int):
        self._registry_map[register] = value
