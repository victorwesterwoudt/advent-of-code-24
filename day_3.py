import re
from enum import Enum

from src import Day


class State(Enum):
    DO = "do()"
    DONT = "don't()"


class Day3(Day):
    pass

    @property
    def data(self) -> list[str]:
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        output = []
        for line in self.raw_data:
            matches = re.findall(pattern, line)
            for match in matches:
                output.append(match)

        return output

    def part_1(self) -> int:
        ans = 0
        for match in self.data:
            if match != "do()" and match != "don't()":
                mul = tuple(map(int, match[4:-1].split(",")))
                ans += mul[0] * mul[1]
        return ans

    def part_2(self) -> int:
        ans = 0
        state = State.DO
        for match in self.data:
            if match != "do()" and match != "don't()":
                mul = tuple(map(int, match[4:-1].split(",")))
                if state == State.DO:
                    ans += mul[0] * mul[1]
                else:
                    continue
            else:
                state = State(match)

        return ans


if __name__ == "__main__":
    day = Day3("./input/day_3.txt")

    print(day.part_1())
    print(day.part_2())
