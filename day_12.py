from collections import deque
from enum import Enum
from functools import cached_property

from src import Day


class Sides(Enum):
    TOP = (-1, 0)
    BOTTOM = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Day12(Day):
    @cached_property
    def data(self):
        return self.raw_data

    def dfs(self, start):
        plot = set()
        perimeter = set()
        stack = deque([start])
        while stack:
            r, c = stack.popleft()

            if (r, c) in plot:
                continue

            plot.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(self.data) and 0 <= nc < len(self.data[0]):
                    if self.data[nr][nc] == self.data[r][c]:
                        stack.append((nr, nc))
                    else:
                        perimeter.add((r, c, Sides((dr, dc))))
                else:
                    perimeter.add((r, c, Sides((dr, dc))))

        return plot, perimeter

    def dfs_sides(
        self,
        start: tuple[int, int, Sides],
        perimeter: set[tuple[int, int, Sides]],
    ):
        edge = set()
        stack = deque([start])
        while stack:
            r, c, side = stack.popleft()

            if (r, c, side) in edge:
                continue

            edge.add((r, c, side))

            if side in [Sides.TOP, Sides.BOTTOM]:
                for dr, dc in [(0, 1), (0, -1)]:
                    if (r + dr, c + dc, side) in perimeter:
                        stack.append((r + dr, c + dc, side))
            elif side in [Sides.LEFT, Sides.RIGHT]:
                for dr, dc in [(1, 0), (-1, 0)]:
                    if (r + dr, c + dc, side) in perimeter:
                        stack.append((r + dr, c + dc, side))

        return edge

    def plots_and_perimeters(self):
        visited = set()
        output = []
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                if (r, c) not in visited:
                    plot, perimeter = self.dfs((r, c))
                    visited.update(plot)
                    output.append((plot, perimeter))
        return output

    def part_1(self):
        return sum(
            [
                len(plot) * len(perimeter)
                for plot, perimeter in self.plots_and_perimeters()
            ]
        )

    def part_2(self):
        results = day.plots_and_perimeters()
        ans = 0
        for plot, perimeter in results:
            sides = 0
            visited = set()
            for start in perimeter:
                if start in visited:
                    continue

                side = self.dfs_sides(start, perimeter)
                visited.update(side)
                sides += 1

            ans += len(plot) * sides

        return ans


if __name__ == "__main__":
    day = Day12("./input/day_12.txt")
    print(day.part_1())
    print(day.part_2())
