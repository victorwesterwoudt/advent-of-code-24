from enum import Enum
from functools import cached_property

from src import Day


class Move(Enum):
    delta: tuple[int, int]

    UP = "^", (-1, 0)
    DOWN = "v", (1, 0)
    LEFT = "<", (0, -1)
    RIGHT = ">", (0, 1)

    def __new__(cls, symbol, delta):
        obj = object.__new__(cls)
        obj._value_ = symbol
        obj.delta = delta
        return obj


class Day15(Day):
    @cached_property
    def data(self) -> tuple[list[list[str]], list[Move]]:
        with open(self._input) as file:
            grid, moves = file.read().split("\n\n")

        grid = [list(row) for row in grid.split("\n")]

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "@":
                    start = (r, c)
                    break

        return (
            start,
            grid,
            [Move(move) for move in moves.replace("\n", "")],
        )

    @property
    def start(self) -> tuple[int, int]:
        return self.data[0]

    @property
    def grid(self) -> list[list[str]]:
        return self.data[1]

    @property
    def moves(self) -> list[Move]:
        return self.data[2]

    @staticmethod
    def print_grid(grid: list[list[str]]) -> None:
        return "\n".join(["".join(row) for row in grid])

    def move(
        self, r: int, c: int, move: Move, grid: list[list[str]]
    ) -> tuple[int, int]:
        dr, dc = move.delta
        nr = r + dr
        nc = c + dc

        if grid[nr][nc] == "O":
            self.move(nr, nc, move, grid)

        if grid[nr][nc] == "#":
            return 0, 0
        elif grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return move.delta

        return 0, 0

    def part_1(self) -> int:
        r, c = self.start
        grid = self.grid
        for move in self.moves:
            dr, dc = self.move(r, c, move, grid)
            r += dr
            c += dc

        return grid


if __name__ == "__main__":
    day = Day15("./input/day_15.txt")
    print(day.print_grid(day.part_1()))
