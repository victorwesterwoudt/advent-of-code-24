import heapq
import time
from enum import Enum
from functools import cached_property

from src import Day


class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

    def __lt__(self, other):
        if isinstance(other, Direction):
            return self.name < other.name
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Direction):
            return self.name <= other.name
        return NotImplemented

    def __repr__(self):
        return self.name.lower()


class Day16(Day):
    @cached_property
    def data(self):
        grid = self.raw_data
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "S":
                    start = (r, c)
                elif cell == "E":
                    end = (r, c)

        return start, end, grid

    @cached_property
    def grid(self):
        return self.data[2]

    @property
    def start(self) -> tuple[int, int, Direction]:
        return (*self.data[0], Direction.EAST)

    @property
    def end(self) -> tuple[int, int]:
        return self.data[1]

    def solve(self, start, end):
        start_r, start_c, start_d = start
        end_r, end_c = end
        memo = {}
        heap = [(0, start_r, start_c, start_d)]

        while heap:
            cost, r, c, d = heapq.heappop(heap)

            if (r, c) == (end_r, end_c):
                return cost, d

            if (r, c) in memo and cost >= memo[(r, c)][0]:
                continue

            memo[(r, c)] = (cost, d)

            for direction in Direction:
                dr, dc = direction.value
                nr, nc = r + dr, c + dc
                if self.grid[nr][nc] != "#":
                    if direction == d:
                        new_cost = cost + 1
                    else:
                        new_cost = cost + 1001
                    heapq.heappush(
                        heap,
                        (new_cost, nr, nc, direction),
                    )

        return float("inf"), None

    def print_grid(self, grid):
        return "\n".join(grid)

    def part_1(self) -> int:
        cost, _ = self.solve(self.start, self.end)
        return cost

    def part_2(self) -> int:
        min_cost, _ = self.solve(self.start, self.end)

        # visited = set([(r, c) for r, c, d in path])
        perc_done = 0
        ans = 1
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell != "#":
                    c1, d1 = self.solve(self.start, (r, c))

                    if c1 >= min_cost:
                        continue

                    c2, _ = self.solve((r, c, d1), self.end)

                    if c1 + c2 == min_cost:
                        ans += 1

                perc_done += 1
                if perc_done % 100 == 0:
                    print(
                        f"{perc_done / (len(self.grid) * len(self.grid[0])) * 100:.2f}% done"
                    )

        return ans


if __name__ == "__main__":
    day = Day16("./input/day_16.txt")

    start_time = time.time()
    p1 = day.part_1()
    end_time = time.time()

    p2 = day.part_2()

    print(f"Part 1 result: {p1}")
    print(f"Part 2 result: {p2}")
    print(f"Time taken: {end_time - start_time:.2f}s")
