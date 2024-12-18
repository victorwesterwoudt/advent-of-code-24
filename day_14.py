import re
from collections import defaultdict
from functools import cached_property

from src import Day


class Day14(Day):
    @cached_property
    def data(self):
        output = []
        for line in self.raw_data:
            output.append(tuple(map(int, re.findall(r"-?\d+", line))))

        return output

    def calc_locations(self, n, C, R):
        grid = defaultdict(int)
        for pc, pr, vc, vr in self.data:
            nc = (pc + vc * n) % C
            nr = (pr + vr * n) % R
            grid[(nc, nr)] += 1
        return grid

    def draw_grid(self, n, C, R):
        robots = self.calc_locations(n, C, R)
        grid = [["." for _ in range(C)] for _ in range(R)]
        for (c, r), n in robots.items():
            grid[r][c] = "#" if n >= 1 else "."

        return "\n".join(["".join(row) for row in grid])

    def calc_score(self, n, C, R):
        grid = self.calc_locations(n, C, R)
        quadrants = defaultdict(int)
        for (c, r), n in grid.items():
            if c < C // 2:
                if r < R // 2:
                    quadrants[0] += n
                elif r > R // 2:
                    quadrants[3] += n
            elif c > C // 2:
                if r < R // 2:
                    quadrants[1] += n
                elif r > R // 2:
                    quadrants[2] += n

        return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    def part_1(self) -> int:
        C = 101
        R = 103
        n = 100
        return self.calc_score(n, C, R)

    def part_2(self) -> int:
        min_score = float("inf")
        min_n = 0
        n = 0
        for n in range(10000):
            score = self.calc_score(n, 101, 103)
            if score < min_score:
                min_score = score
                min_n = n

        print(self.draw_grid(min_n, 101, 103))
        return min_n


if __name__ == "__main__":
    d = Day14("./input/day_14.txt")
    print(d.part_1())
    print(d.part_2())
