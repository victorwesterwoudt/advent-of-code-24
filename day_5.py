from collections import defaultdict
from functools import cached_property

from src import Day


class Day5(Day):
    @cached_property
    def data(self) -> list[str]:
        split = self.raw_data.index("")

        rules = defaultdict(set)
        for line in self.raw_data[:split]:
            i, r = tuple(map(int, line.split("|")))
            rules[i].add(r)

        updates = []
        for line in self.raw_data[split + 1 :]:
            updates.append(tuple(map(int, line.split(","))))

        return rules, updates

    @cached_property
    def rules(self) -> dict[int, set[int]]:
        return self.data[0]

    @cached_property
    def updates(self):
        return self.data[1]

    def analyze_update(self, update: list[int]) -> list[bool]:
        output = []
        for i, page in enumerate(update):
            before = set(update[:i])
            if before & self.rules[page]:
                output.append(False)
            else:
                output.append(True)
        return output

    def is_valid_update(self, update: list[int]) -> bool:
        return all(self.analyze_update(update))

    def part_1(self) -> int:
        ans = 0
        for update in self.updates:
            if self.is_valid_update(update):
                ans += update[len(update) // 2]
        return ans

    def part_2(self) -> int:
        ans = 0
        for update in self.updates:
            uc = list(update)
            while not all(analysis := self.analyze_update(uc)):
                bad_idx = analysis.index(False)
                bad_page = uc[bad_idx]
                before = uc[: analysis.index(False)]
                swap_idx = min(
                    [
                        i
                        for i, x in enumerate(before)
                        if x in self.rules[bad_page]
                    ]
                )
                uc[bad_idx], uc[swap_idx] = (
                    uc[swap_idx],
                    uc[bad_idx],
                )

            ans += uc[len(uc) // 2]

        return ans


if __name__ == "__main__":
    day = Day5("./input/day_5.txt")
    # print(day.data)
    print(day.part_1())
    print(day.part_2() - day.part_1())
