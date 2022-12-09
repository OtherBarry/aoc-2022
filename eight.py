from base import Problem

import numpy as np

def test_array_visibility(array: np.ndarray, mask: np.ndarray) -> None:
    current_max = -1
    for i, v in enumerate(array):
        if v > current_max:
            current_max = v
            mask[i] = True
    current_max = -1
    for i, v in reversed(list(enumerate(array))):
        if v > current_max:
            current_max = v
            mask[i] = True


class Problem8(Problem):
    def setup(self) -> None:
        grid = []
        for line in self.raw_input.splitlines():
            row = []
            for char in line:
                row.append(int(char))
            grid.append(row)
        self.grid = np.asarray(grid, dtype=np.uint8)

    def part_1(self) -> int:
        binary_map = np.zeros(self.grid.shape, dtype=np.bool)
        for i in range(99):
            test_array_visibility(self.grid[i], binary_map[i])
            test_array_visibility(self.grid[:, i], binary_map[:, i])
        return np.sum(binary_map)

    def part_2(self) -> int:
        return "TBD"
