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
    print(f"Most calories held by single elf: {elves[0].total_calories()}")
    print(
        f"Calories held by top 3 elves: {sum(elf.total_calories() for elf in elves[:3])}"
    )
