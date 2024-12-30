import heapq
from functools import cached_property

from src import Day


class Day18(Day):
    @cached_property
    def data(self):
        corrupted = []
        for line in self.raw_data:
            corrupted.append(tuple(map(int, line.split(","))))

        return corrupted

    def solve(self, start, end, n):
        start_r, start_c = start
        end_r, end_c = end
        memo = {}
        heap = [(0, start_r, start_c)]

        while heap:
            cost, r, c = heapq.heappop(heap)

            if (r, c) == (end_r, end_c):
                return cost

            if (r, c) in memo and cost >= memo[(r, c)]:
                continue

            memo[(r, c)] = cost

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    (nr, nc) not in self.data[:n]
                    and nr >= 0
                    and nc >= 0
                    and nr <= end_r
                    and nc <= end_c
                ):
                    new_cost = cost + 1
                    heapq.heappush(
                        heap,
                        (new_cost, nr, nc),
                    )

        return None

    def part_1(self):
        return self.solve((0, 0), (70, 70), 1024)

    def part_2(self):
        step = 1000
        n = 0
        while True:
            result = self.solve((0, 0), (70, 70), n)
            if not result:
                if step != 1:
                    n -= step
                    step //= 2
                else:
                    break

            n += step

        return ",".join(map(str, self.data[n - 1]))


if __name__ == "__main__":
    day = Day18("./input/day_18.txt")
    print(day.part_1())
    print(day.part_2())
