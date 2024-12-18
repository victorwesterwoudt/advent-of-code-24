import re
from functools import cached_property

from src import Day


class Day13(Day):
    @cached_property
    def data(self):
        output = []
        with open(self._input) as f:
            input = f.read().split("\n\n")

        for block in input:
            output.append(tuple(map(int, re.findall(r"\d+", block))))

        return output

    def solve(self, ax, ay, bx, by, px, py):
        na = (by * px - bx * py) / (ax * by - ay * bx)
        nb = (px - na * ax) / bx

        if na % 1 == nb % 1 == 0:
            return int(na * 3 + nb)
        else:
            return 0

    def part_1(self) -> int:
        ans = 0
        for machine in self.data:
            ans += self.solve(*machine)
        return ans

    def part_2(self) -> int:
        ans = 0
        for ax, ay, bx, by, px, py in self.data:
            ans += self.solve(
                ax, ay, bx, by, px + 10000000000000, py + 10000000000000
            )

        return ans


if __name__ == "__main__":
    day = Day13("./input/day_13.txt")
    print(day.part_1())
    print(day.part_2())
