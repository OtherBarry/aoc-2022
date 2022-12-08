from copy import deepcopy
from dataclasses import dataclass, field

from base import Problem


def chunk_string(string: str, chunk_size: int) -> list[str]:
    return [string[i : i + chunk_size] for i in range(0, len(string), chunk_size)]


@dataclass
class Stack:
    contents: list[str] = field(default_factory=list)

    def push(self, value: str) -> None:
        self.contents.append(value)

    def pop(self) -> str:
        return self.contents.pop()

    def peek(self) -> str:
        return self.contents[-1]


@dataclass
class Supplies:
    stacks: list[Stack]

    def move_9000(self, source: int, target: int, count: int) -> None:
        for _ in range(count):
            self.stacks[target].push(self.stacks[source].pop())

    def move_9001(self, source: int, target: int, count: int) -> None:
        temp_stack = Stack()
        for _ in range(count):
            temp_stack.push(self.stacks[source].pop())
        for _ in range(count):
            self.stacks[target].push(temp_stack.pop())


class Problem5(Problem):
    def setup(self) -> None:
        # TODO: Don't hardcode the height and number of stacks
        lines = self.raw_input.splitlines()
        stack_lines = lines[:8]
        stacks = [Stack() for _ in range(9)]
        stack_lines = stack_lines[::-1]  # reverse so  stacks are in correct order
        for line in stack_lines:
            chunks = chunk_string(line, 4)
            for i, chunk in enumerate(chunks):
                if chunk != "    ":
                    stacks[i].push(chunk[1])
        self.supplies = Supplies(stacks)
        self.moves = []
        for line in lines[10:]:
            _, count, _, source, _, target = line.split()
            self.moves.append((int(source) - 1, int(target) - 1, int(count)))

    def part_1(self) -> str:
        supplies = deepcopy(self.supplies)
        for move in self.moves:
            supplies.move_9000(*move)
        return "".join(stack.peek() for stack in supplies.stacks)

    def part_2(self) -> str:
        supplies = deepcopy(self.supplies)
        for move in self.moves:
            supplies.move_9001(*move)
        return "".join(stack.peek() for stack in supplies.stacks)
