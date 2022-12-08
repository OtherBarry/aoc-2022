from abc import ABC, abstractmethod
from typing import Any


class Problem(ABC):
    def __init__(self, input_path: str):
        with open(input_path) as f:
            self.raw_input = f.read()

    def setup(self) -> None:
        pass

    @abstractmethod
    def part_1(self) -> Any:
        pass

    @abstractmethod
    def part_2(self) -> Any:
        pass

    def run(self) -> None:
        self.setup()
        print(f"Part 1: {self.part_1()}")
        print(f"Part 2: {self.part_2()}")
