from .base import Solution


class SandGrain:
    def __init__(self, max_x: int, max_y: int):
        self.coordinates = (500, 0)
        self.max_x = max_x
        self.max_y = max_y

    def coordinates_in_bounds(self, x, y):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def move_once(self, valid_coordinates: set[tuple[int, int]]) -> bool:
        x, y = self.coordinates
        for move in (
            (x, y + 1),  # Down
            (x - 1, y + 1),  # Down left
            (x + 1, y + 1),  # Down right
        ):
            if not self.coordinates_in_bounds(*move):
                raise ValueError("Sand grain has fallen out of bounds")
            if move in valid_coordinates:
                self.coordinates = move
                return True
        return False

    def move(self, valid_coordinates: set[tuple[int, int]]) -> bool:
        while self.move_once(valid_coordinates):
            pass


class Solution14(Solution):
    def setup(self) -> None:
        values = []
        max_x = 0
        max_y = 0
        for line in self.raw_input.splitlines():
            line_values = []
            for coordinate_pair in line.split(" -> "):
                coordinates = tuple(int(c) for c in coordinate_pair.split(","))
                max_x = max(max_x, coordinates[0])
                max_y = max(max_y, coordinates[1])
                line_values.append(coordinates)
            values.append(line_values)
        accessible_coordinates = set()
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                accessible_coordinates.add((x, y))
        for line in values:
            for i in range(1, len(line)):
                start = line[i - 1]
                end = line[i]
                if start[0] == end[0]:
                    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                        accessible_coordinates.discard((start[0], y))
                elif start[1] == end[1]:
                    for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                        accessible_coordinates.discard((x, start[1]))
        self.accessible_coordinates = accessible_coordinates
        self.max_x = max_x
        self.max_y = max_y

    def part_1(self) -> int:
        count = 0
        while True:
            count += 1
            grain = SandGrain(self.max_x, self.max_y)
            try:
                grain.move(self.accessible_coordinates)
            except ValueError:
                return count - 1
            self.accessible_coordinates.discard(grain.coordinates)

    def part_2(self) -> int:
        return "TBD"
