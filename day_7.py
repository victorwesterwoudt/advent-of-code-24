from src import Day


class Day7(Day):
    @property
    def data(self) -> list[str]:
        output = []
        for line in self.raw_data:
            result, vars = line.split(": ")
            result = int(result)
            vars = tuple(map(int, vars.split(" ")))
            output.append((result, vars))

        return output

    @classmethod
    def is_valid(
        cls, result: int, vars: tuple[int], part2: bool = False
    ) -> bool:
        if len(vars) == 1:
            return result == vars[0]
        if cls.is_valid(result, (vars[0] + vars[1], *vars[2:]), part2):
            return True
        if cls.is_valid(result, (vars[0] * vars[1], *vars[2:]), part2):
            return True
        if part2 and cls.is_valid(
            result, (int(str(vars[0]) + str(vars[1])), *vars[2:]), part2
        ):
            return True
        return False

    def part_1(self) -> int:
        ans = 0
        for result, vars in self.data:
            if self.is_valid(result, vars):
                ans += result

        return ans

    def part_2(self) -> int:
        ans = 0
        for result, vars in self.data:
            if self.is_valid(result, vars, part2=True):
                ans += result

        return ans


if __name__ == "__main__":
    day = Day7("./input/day_7.txt")
    print(day.part_1())
    print(day.part_2())
