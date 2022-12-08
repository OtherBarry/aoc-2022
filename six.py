from base import Problem


class MaxLengthStack:
    # TODO: Optimise unique-ness check
    def __init__(self, max_length=4):
        self.max_length = max_length
        self._stack = []

    def push(self, value):
        if len(self._stack) == self.max_length:
            self._stack.pop(0)
        self._stack.append(value)

    def is_unique(self):
        return len(self._stack) == self.max_length and len(set(self._stack)) == len(
            self._stack
        )


class Problem6(Problem):
    def setup(self) -> None:
        pass

    def part_1(self) -> int:
        stack = MaxLengthStack(4)
        for i, v in enumerate(self.raw_input):
            stack.push(v)
            if stack.is_unique():
                return i + 1

    def part_2(self) -> str:
        stack = MaxLengthStack(14)
        for i, v in enumerate(self.raw_input):
            stack.push(v)
            if stack.is_unique():
                return i + 1
