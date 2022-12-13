from .base import Solution


def compare(left, right) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        return None
    if isinstance(left, list) and isinstance(right, list):
        count = 0
        while True:
            try:
                left_item = left[count]
            except IndexError:
                if len(left) == len(right):
                    return None
                return True
            try:
                right_item = right[count]
            except IndexError:
                return False
            result = compare(left_item, right_item)
            if result is not None:
                return result
            count += 1
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])
    raise TypeError(f"Cannot compare {left} and {right}")


class Packet:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return compare(self.value, other.value)


class Solution13(Solution):
    def setup(self) -> None:
        pairs = []
        for pair in self.raw_input.split("\n\n"):
            first, second = pair.splitlines()
            pairs.append((eval(first), eval(second)))
        self.pairs = pairs

    def part_1(self) -> int:
        sum = 0
        for index, pair in enumerate(self.pairs):
            if compare(*pair):
                sum += index + 1
        return sum

    def part_2(self) -> int:
        packets = []
        for left, right in self.pairs:
            packets.append(Packet(left))
            packets.append(Packet(right))
        packets.append(Packet([[2]]))
        packets.append(Packet([[6]]))
        packets.sort()
        index2 = packets.index(Packet([[2]])) + 1
        index6 = packets.index(Packet([[6]])) + 1
        return index2 * index6
