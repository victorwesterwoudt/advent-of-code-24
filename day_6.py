import copy
from enum import Enum
from functools import cached_property

from src import Day


class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def rot(self):
        match self:
            case Directions.UP:
                return Directions.RIGHT
            case Directions.LEFT:
                return Directions.UP
            case Directions.DOWN:
                return Directions.LEFT
            case Directions.RIGHT:
                return Directions.DOWN


class Day6(Day):
    @cached_property
    def data(self) -> list[list[str]]:
        for row, line in enumerate(self.raw_data):
            for col, c in enumerate(line):
                if c == "^":
                    start = (row, col)

        return start, [list(line) for line in self.raw_data]

    @cached_property
    def start(self) -> tuple[int, int]:
        return self.data[0]

    @cached_property
    def grid(self) -> list[list[str]]:
        return self.data[1]

    @staticmethod
    def find_path(
        grid: list[list[str]],
        start: tuple[int, int],
        direction: Directions = Directions.UP,
    ) -> set[tuple[int, int]]:
        visited = {(direction, *start)}
        r, c = start
        isloop = False
        while True:
            rn, cn = r + direction.value[0], c + direction.value[1]
            if rn < 0 or rn >= len(grid) or cn < 0 or cn >= len(grid[0]):
                isloop = False
                break
            elif grid[rn][cn] == "#":
                direction = direction.rot()
            else:
                r, c = rn, cn
                if (direction, r, c) in visited:
                    isloop = True
                    break
                else:
                    visited.add((direction, r, c))

        return visited, isloop

    def part_1(self) -> int:
        path, _ = self.find_path(self.grid, self.start)
        return len(set([x[1:] for x in path]))

    def part_2(self) -> int:
        ans = 0
        (original_path, _) = self.find_path(self.grid, self.start)
        obstruction_locations = set([x[1:] for x in original_path])
        obstruction_locations.remove(self.start)
        for loc in obstruction_locations:
            grid = copy.deepcopy(self.grid)
            grid[loc[0]][loc[1]] = "#"
            _, isloop = self.find_path(grid, self.start)
            if isloop:
                ans += 1

        return ans


if __name__ == "__main__":
    d = Day6("./input/day_6.txt")
    print(len(d.grid), len(d.grid[0]))

    print(d.part_1())
    print(d.part_2())
