from enum import Enum
from functools import cached_property

from src import Day


class Step(Enum):
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
    def data(self) -> tuple[list[list[str]], list[Step]]:
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
            [Step(move) for move in moves.replace("\n", "")],
        )

    @property
    def start(self) -> tuple[int, int]:
        return self.data[0]

    @property
    def grid(self) -> list[list[str]]:
        return self.data[1]

    @property
    def moves(self) -> list[Step]:
        return self.data[2]

    @staticmethod
    def print_grid(grid: list[list[str]]) -> None:
        return "\n".join(["".join(row) for row in grid])

    def move(
        self, r: int, c: int, step: Step, grid: list[list[str]]
    ) -> tuple[int, int]:
        dr, dc = step.delta
        nr = r + dr
        nc = c + dc

        if grid[nr][nc] == "O":
            self.move(nr, nc, step, grid)

        if grid[nr][nc] == "#":
            return False
        elif grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return True

        return False

    def move2(self, r: list[int], c: list[int], move: Step, grid):
        dr, dc = move.delta

        nr, nc = r + dr, c + dc

        if grid[nr][nc] == "#":
            return 0, 0
        elif grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return move.delta
        elif grid[nr][nc] == "[":
            first = self.move2(nr, nc, move, grid)
            second = self.move2(nr, nc + 1, move, grid)

            if first and not second:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                return 0, 0
            elif second and not first:
                grid[r][c + 1], grid[nr][nc + 1] = (
                    grid[nr][nc + 1],
                    grid[r][c + 1],
                )
                return 0, 0
        elif grid[nr][nc] == "]":
            first = self.move2(nr, nc, move, grid)
            second = self.move2(nr, nc - 1, move, grid)

            if first and not second:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                return 0, 0
            elif second and not first:
                grid[r][c - 1], grid[nr][nc - 1] = (
                    grid[nr][nc - 1],
                    grid[r][c - 1],
                )
                return 0, 0

        return 0, 0

    def part_1(self) -> int:
        r, c = self.start
        grid = self.grid

        for move in self.moves:
            if self.move(r, c, move, grid):
                r += move.delta[0]
                c += move.delta[1]

        ans = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "O":
                    ans += 100 * r + c

        return ans

    @cached_property
    def data2(self) -> list[list[str]]:
        grid = self.grid
        dgrid: list[list[str]] = []
        start: tuple[int, int]
        for r, row in enumerate(grid):
            dgrid.append([])
            for c, cell in enumerate(row):
                if cell == "#":
                    dgrid[r].extend(["#", "#"])
                elif cell == "O":
                    dgrid[r].extend(["[", "]"])
                elif cell == "@":
                    dgrid[r].extend(["@", "."])
                else:
                    dgrid[r].extend([cell, cell])

        for r, row in enumerate(dgrid):
            for c, cell in enumerate(row):
                if cell == "@":
                    start = (r, c)

        return start, dgrid

    @property
    def start2(self) -> tuple[int, int]:
        return self.data2[0]

    @property
    def grid2(self) -> list[list[str]]:
        return self.data2[1]


if __name__ == "__main__":
    day = Day15("./input/day_15.txt")
    print(day.part_1())
    
