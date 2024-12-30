from functools import cached_property

from src import Day


class Day19(Day):
    @cached_property
    def data(self):
        with open(self._input, "r") as file:
            towels, patterns = file.read().split("\n\n")

        return towels.split(", "), patterns.split("\n")

    @property
    def towels(self):
        return sorted(self.data[0], key=len, reverse=False)

    @property
    def patterns(self):
        return self.data[1]

    def solve(
        self, pattern: str, towels: list[str], memo: dict | None = None
    ) -> bool:
        if memo is None:
            memo = {}

        if pattern in memo:
            return memo[pattern]

        if not pattern:
            return True

        count = 0
        for towel in towels:
            if pattern.startswith(towel):
                count += self.solve(pattern[len(towel) :], towels, memo)

        memo[pattern] = count
        return count

    def part_1(self):
        ans = 0
        for pattern in self.patterns:
            if self.solve(pattern, self.towels):
                ans += 1

        return ans

    def part_2(self):
        ans = 0
        for pattern in self.patterns:
            ans += self.solve(pattern, self.towels)

        return ans


if __name__ == "__main__":
    day = Day19("./input/day_19.txt")
    print(day.part_1())
    print(day.part_2())
