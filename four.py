from base import Problem


class Problem4(Problem):
    def setup(self) -> None:
        pairs = []
        for line in self.raw_input.splitlines():
            pair = []
            for elf in line.split(","):
                start, end = elf.split("-")
                pair.append(set(range(int(start), int(end) + 1)))
            pairs.append(pair)
        self.pairs = pairs

    def part_1(self) -> int:
        result = 0
        for a, b in self.pairs:
            intersection = a & b
            if a == intersection or b == intersection:
                result += 1
        return result

    def part_2(self) -> int:
        result = 0
        for a, b in self.pairs:
            intersection = a & b
            if intersection:
                result += 1
        return result
