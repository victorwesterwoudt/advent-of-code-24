from collections import defaultdict

from src import Day


class Day8(Day):
    @property
    def data(self) -> dict[str, list[tuple[int, int]]]:
        antennae = defaultdict(list)
        for r, line in enumerate(self.raw_data):
            for c, char in enumerate(line):
                if char != ".":
                    antennae[char].append((r, c))

        return antennae

    @staticmethod
    def pairs(
        antennae: list[tuple[int, int]],
    ) -> dict[tuple[tuple[int, int], tuple[int, int]], tuple[int, int]]:
        output = {}
        for i, a in enumerate(antennae):
            for j in range(i + 1, len(antennae)):
                pair = (a, antennae[j])
                output[pair] = (
                    pair[0][0] - pair[1][0],
                    pair[0][1] - pair[1][1],
                )
        return output

    @property
    def result(self) -> int:
        p1 = set()
        p2 = set()
        for _, antennae in self.data.items():
            pairs = self.pairs(antennae)
            for p, d in pairs.items():
                n = 0
                while True:
                    an = (p[0][0] + n * d[0], p[0][1] + n * d[1])
                    if 0 <= an[0] < len(self.raw_data) and 0 <= an[1] < len(
                        self.raw_data[0]
                    ):
                        if n == 1:
                            p1.add(an)

                        p2.add(an)
                    else:
                        break

                    n += 1

                n = 0
                while True:
                    an = (p[1][0] - n * d[0], p[1][1] - n * d[1])
                    if 0 <= an[0] < len(self.raw_data) and 0 <= an[1] < len(
                        self.raw_data[0]
                    ):
                        if n == 1:
                            p1.add(an)

                        p2.add(an)
                    else:
                        break
                    n += 1

        return len(p1), len(p2)

    def part_1(self) -> int:
        return self.result[0]

    def part_2(self) -> int:
        return self.result[1]


if __name__ == "__main__":
    day = Day8("./input/day_8.txt")
    print(day.part_1())
    print(day.part_2())
