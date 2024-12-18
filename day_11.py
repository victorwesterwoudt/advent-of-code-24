from collections import defaultdict
from functools import cached_property

from src import Day


class Day11(Day):
    @cached_property
    def data(self):
        return list(self.raw_data[0].split())

    def blink(self, stones: dict[str:int]) -> dict[str:int]:
        output = defaultdict(int)
        for stone, repl in stones.items():
            match stone:
                case _ if len(stone) % 2 == 0:
                    midpt = len(stone) // 2
                    left = stone[:midpt]
                    right = stone[midpt:].lstrip("0")
                    output[left] += repl
                    output[right if right else "0"] += repl
                case "0":
                    output["1"] += repl
                case _:
                    output[str(int(stone) * 2024)] += repl
        return output

    def part_1(self) -> int:
        data = {stone: 1 for stone in self.data}
        for _ in range(25):
            data = self.blink(data)

        return sum(data.values())

    def part_2(self) -> int:
        data = {stone: 1 for stone in self.data}
        for _ in range(75):
            data = self.blink(data)

        return sum(data.values())


if __name__ == "__main__":
    day = Day11("./input/day_11.txt")
    print(day.part_1())
    print(day.part_2())
