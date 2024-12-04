from enum import Enum

from src import Day


class Directions(Enum):
    HORIZONTAL_RIGHT = (0, 1)
    VERTICAL_DOWN = (1, 0)
    DIAGONAL_RIGHT_UP = (1, -1)
    DIAGONAL_RIGHT_DOWN = (1, 1)
    HORIZONTAL_LEFT = (0, -1)
    VERTICAL_UP = (-1, 0)
    DIAGONAL_LEFT_UP = (-1, -1)
    DIAGONAL_LEFT_DOWN = (-1, 1)


class Day4(Day):
    @property
    def data(self) -> list[list[str]]:
        output = []
        for line in self.raw_data:
            output.append(list(line))

        return output

    def part_1(self) -> int:
        ans = 0
        potential_starts = []
        for r, line in enumerate(self.data):
            for c, character in enumerate(line):
                if character == "X":
                    potential_starts.append((r, c))

        for start in potential_starts:
            for direction in Directions:
                word = "X"
                r = start[0] + direction.value[0]
                c = start[1] + direction.value[1]
                while True:
                    if (
                        r < 0
                        or r >= len(self.data)
                        or c < 0
                        or c >= len(self.data[0])
                    ):
                        break

                    word += self.data[r][c]
                    if word not in "XMAS":
                        break
                    if word == "XMAS":
                        ans += 1
                        break

                    r += direction.value[0]
                    c += direction.value[1]

        return ans

    def part_2(self) -> int:
        potential_centers = []
        ans = 0
        xmasses = [
            "MSMS",
            "MSSM",
            "SMMS",
            "SMSM",
        ]
        dxs = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        for r, line in enumerate(self.data):
            for c, character in enumerate(line):
                if character == "A":
                    potential_centers.append((r, c))

        for center in potential_centers:
            word = ""
            for dx in dxs:
                r = center[0] + dx[0]
                c = center[1] + dx[1]
                if (
                    r < 0
                    or r >= len(self.data)
                    or c < 0
                    or c >= len(self.data[0])
                ):
                    break

                word += self.data[r][c]

            if word in xmasses:
                ans += 1

        return ans


if __name__ == "__main__":
    day = Day4("./input/day_4.txt")
    print(day.part_1())
    print(day.part_2())
