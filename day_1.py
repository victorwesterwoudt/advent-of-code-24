from src import Day


class Day1(Day):
    @property
    def data(self) -> tuple[list[int], list[int]]:
        return tuple(
            sorted(x)
            for x in zip(*[list(map(int, x.split())) for x in self.raw_data])
        )

    def part_1(self) -> int:
        return sum(abs(x - y) for x, y in zip(*self.data))

    def part_2(self) -> int:
        left, right = self.data
        return sum([x * right.count(x) for x in left])


if __name__ == "__main__":
    day = Day1("./input/day_1.txt")
    print(day.part_1())
    print(day.part_2())
