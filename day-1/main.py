from dataclasses import dataclass


@dataclass
class Elf:
    inventory: list[int]

    def total_calories(self) -> int:
        return sum(self.inventory)


with open("day-1/input.txt") as f:
    input = f.read().splitlines()
    elves = []
    elf = Elf([])
    for line in input:
        if line == "":
            elves.append(elf)
            elf = Elf([])
        else:
            elf.inventory.append(int(line))
    elves.sort(key=lambda elf: elf.total_calories(), reverse=True)
    print(f"Part 1: {elves[0].total_calories()}")
    print(f"Part 2: {sum(elf.total_calories() for elf in elves[:3])}")
