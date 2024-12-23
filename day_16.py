import heapq
import sys
from enum import Enum
from functools import cached_property

from src import Day

sys.setrecursionlimit(10000)


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

    # def solve(self, r, c, d, cost, end, memo):
    #     if (r, c) == end:
    #         return cost

    #     if (r, c) in memo and cost >= memo[(r, c)][0]:
    #         return float("inf")

    #     memo[(r, c)] = (cost, d)

    #     min_cost = float("inf")
    #     for direction in Direction:
    #         dr, dc = direction.value
    #         nr, nc = r + dr, c + dc
    #         if (
    #             0 <= nr < len(self.grid)
    #             and 0 <= nc < len(self.grid[0])
    #             and self.grid[nr][nc] != "#"
    #         ):
    #             if direction == d:
    #                 new_cost = cost + 1
    #             else:
    #                 new_cost = cost + 1001
    #             min_cost = min(
    #                 min_cost,
    #                 self.solve(nr, nc, direction, new_cost, end, memo),
    #             )

    #     return min_cost

    def solve(self):
        start_r, start_c, start_d = self.start
        end_r, end_c = self.end
        memo = {}
        heap = [(0, start_r, start_c, start_d)]

        while heap:
            cost, r, c, d = heapq.heappop(heap)

            if (r, c) == (end_r, end_c):
                return cost

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

        return float("inf"), []

    def part_1(self) -> int:
        return self.solve()

    def print_grid(self, grid):
        return "\n".join(grid)

    def part_2(self) -> int:
        pass


if __name__ == "__main__":
    day = Day16("./input/day_16.txt")
    p1 = day.part_1()
    print(p1)
    # for route in p1[1]:
    #     for tile in route:
    #         tiles.add(tile)
    # print(len(tiles))


# path finding:
# the input of the pathfinding function is:
# - the my current location
# - the cost of reaching this location
# - the direcition I\m facing
# - the end location
# - a list (memo) of visited locations and the cost of reaching them

# if my location is the end location, I return the cost of reaching this location
# if else my location is in the memo, and the cost of reaching this location is less than the cost in the memo, I update the memo
# I then try to move in all directions and for each direction add the cost of moving in that direction to the cost of reaching the current location
# I then recursively call the function with the new location, the new cost, the new direction, the end location, and the memo
