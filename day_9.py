from collections import deque

from src import Day


class Day9(Day):
    @property
    def data(self) -> list[int]:
        output = []
        data = tuple(map(int, self.raw_data[0]))
        for i, d in enumerate(data):
            if i % 2 == 0:
                output.append([i // 2] * d)
            else:
                output.append([None] * d)

        return output

    def part_1(self) -> int:
        input = deque([item for sublist in self.data for item in sublist])
        output = []
        while input:
            first = input.popleft()
            if first is not None:
                output.append(first)
            else:
                while True:
                    i = input.pop()
                    if i is not None:
                        output.append(i)
                        break

        ans = 0
        for i, d in enumerate(output):
            ans += i * int(d)

        return ans

    def part_2(self) -> int:
        input = list(self.data)
        output = []

        while input:
            first = input.pop(0)
            if len(first) != 0 and first[0] is not None:
                output.append(first)
            else:
                inserted = False
                for i in range(len(input) - 1, -1, -1):
                    insert = input[i]
                    if len(insert) != 0 and insert[0] is not None:
                        if len(insert) == len(first):
                            output.append(insert)
                            input[i] = [None] * len(insert)
                            inserted = True
                            break
                        elif len(insert) < len(first):
                            output.append(insert)
                            input[i] = [None] * len(insert)
                            input = [
                                [None] * (len(first) - len(insert))
                            ] + input
                            inserted = True
                            break
                if not inserted:
                    output.append(first)

        output = [item for sublist in output for item in sublist]
        ans = 0
        for i, d in enumerate(output):
            if d is not None:
                ans += i * int(d)

        return ans


if __name__ == "__main__":
    day = Day9("./input/day_9.txt")
    # print(day.data)
    print(day.part_1())
    print(day.part_2())
