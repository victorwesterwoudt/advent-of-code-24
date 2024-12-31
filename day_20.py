from functools import cached_property

from src import Day


class Day20(Day):
    @cached_property
    def data(self) -> list[list[str]]:
        grid = self.raw_data
        S: tuple[int, int] = (0, 0)
        E: tuple[int, int] = (0, 0)
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "S":
                    S = (r, c)
                elif cell == "E":
                    E = (r, c)

        return S, E, grid

    @property
    def start(self):
        return self.data[0]

    @property
    def end(self):
        return self.data[1]

    @cached_property
    def grid(self):
        return [list(row) for row in self.data[2]]

    @cached_property
    def distances(self):
        # this is an alternative to a Breadth First Fill algorithm
        # where we know that there is only one path from S to E
        # so we just need to look if the next cell has not been visited before
        # e.g. we do not need to keep track of all visited cells

        distances = [
            [float("inf")] * len(self.grid[0]) for _ in range(len(self.grid))
        ]
        r, c = self.start

        distances[r][c] = 0

        while self.grid[r][c] != "E":
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0
                    or nc < 0
                    or nr >= len(self.grid)
                    or nc >= len(self.grid[0])
                ):
                    continue
                if self.grid[nr][nc] == "#":
                    continue
                if distances[nr][nc] != float("inf"):
                    continue

                distances[nr][nc] = distances[r][c] + 1
                r, c = nr, nc

        return distances

    def part_1(self):
        ans = 0
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == "#":
                    continue
                for dr, dc in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= len(self.grid)
                        or nc >= len(self.grid[0])
                    ):
                        continue
                    if self.grid[nr][nc] == "#":
                        continue
                    if self.distances[nr][nc] - self.distances[r][c] >= 102:
                        ans += 1

        return ans

    def part_2(self):
        ans = 0

        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == "#":
                    continue
                for radius in range(2, 20 + 1):
                    # manhattan distance
                    for dr in range(radius + 1):
                        dc = radius - dr
                        for nr, nc in {
                            (r + dr, c + dc),
                            (r + dr, c - dc),
                            (r - dr, c + dc),
                            (r - dr, c - dc),
                        }:
                            if (
                                nr < 0
                                or nc < 0
                                or nr >= len(self.grid)
                                or nc >= len(self.grid[0])
                            ):
                                continue
                            if self.grid[nr][nc] == "#":
                                continue
                            if (
                                self.distances[nr][nc] - self.distances[r][c]
                                >= 100 + radius
                            ):
                                ans += 1

        return ans


if __name__ == "__main__":
    day = Day20("./input/day_20.txt")
    # print(day.data)
    print(day.part_1())
    print(day.part_2())
