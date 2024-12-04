from src import Day


class Day2(Day):
    @property
    def data(self) -> list[int]:
        reports = []
        for line in self.raw_data:
            reports.append([int(x) for x in line.split()])
        return reports

    @staticmethod
    def checksafe(report: list[int]) -> bool:
        diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        signs = []
        for diff in diffs:
            if diff == 0 or abs(diff) > 3:
                signs.append(0)
            elif diff > 0:
                signs.append(1)
            elif diff < 0:
                signs.append(-1)
        return abs(sum(signs)) == len(signs)

    def part_1(self) -> int:
        return sum([self.checksafe(report) for report in self.data])

    def part_2(self) -> int:
        return sum(
            [
                any(
                    self.checksafe(report[:i] + report[i + 1 :])
                    for i in range(len(report))
                )
                for report in self.data
            ]
        )


if __name__ == "__main__":
    day = Day2("./input/day_2.txt")
    print(f"Part 1: {day.part_1()}")
    print(f"Part 2: {day.part_2()}")
