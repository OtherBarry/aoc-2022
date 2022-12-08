from base import BaseProblem


class ProblemOne(BaseProblem):
    def setup(self) -> None:
        input_ = self.raw_input.splitlines()
        elves = []
        elf = 0
        for line in input_:
            if line == "":
                elves.append(elf)
                elf = 0
            else:
                elf += int(line)
        elves.sort(reverse=True)
        self.elves = elves

    def part_1(self) -> int:
        return self.elves[0]

    def part_2(self) -> int:
        return sum(self.elves[:3])
