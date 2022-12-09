from abc import ABC, abstractmethod
from timeit import default_timer as timer
from typing import Any


class Problem(ABC):
    def __init__(self, input_path: str):
        with open(input_path) as f:
            self.raw_input = f.read()

    def _time(self, func: Any) -> tuple[str, Any]:
        start = timer()
        result = func()
        end = timer()
        return self._format_time(end - start), result

    @staticmethod
    def _format_time(time: float) -> str:
        if time < 1:
            return f"{time * 1000:.2f} ms"
        else:
            return f"{time:.2f}  s"

    def setup(self) -> None:
        pass

    @abstractmethod
    def part_1(self) -> Any:
        pass

    @abstractmethod
    def part_2(self) -> Any:
        pass

    def run(self) -> None:
        setup_time, _ = self._time(self.setup)
        print(f"\tSetup run in {setup_time}")
        p1_time, p1_result = self._time(self.part_1)
        print(f"\tPart 1 ({p1_time}): {p1_result}")
        p2_time, p2_result = self._time(self.part_2)
        print(f"\tPart 2 ({p2_time}): {p2_result}")
