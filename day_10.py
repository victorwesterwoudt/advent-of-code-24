from collections import deque
from functools import cached_property

from src import Day


class Day10(Day):
    @cached_property
    def data(self):
        trailheads = []
        trailends = []
        grid = []
        for r, line in enumerate(self.raw_data):
            for c, char in enumerate(line):
                if char == "0":
                    trailheads.append((r, c))
                if char == "9":
                    trailends.append((r, c))
            grid.append(list(map(int, line)))

        return trailheads, grid, trailends

    @cached_property
    def trailheads(self):
        return self.data[0]

    @cached_property
    def trailends(self):
        return self.data[2]

    @cached_property
    def grid(self):
        return self.data[1]

    def dfs(self, start):
        ans = 0
        visited = set()
        stack = deque([start])
        while stack:
            r, c = stack.popleft()

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if self.grid[r][c] == 9:
                ans += 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < len(self.grid)
                    and 0 <= nc < len(self.grid[0])
                    and self.grid[nr][nc] == self.grid[r][c] + 1
                ):
                    stack.append((nr, nc))

        return ans

    def dfs2(self, r, c, memo: dict):
        if self.grid[r][c] == 9:
            return 1

        if (r, c) in memo:
            return memo[(r, c)]

        ans = 0

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(self.grid)
                and 0 <= nc < len(self.grid[0])
                and self.grid[nr][nc] == self.grid[r][c] + 1
            ):
                ans += self.dfs2(nr, nc, memo)

        memo[(r, c)] = ans

        return ans

    def part_1(self):
        ans = 0
        for trailhead in self.trailheads:
            ans += self.dfs(trailhead)

        return ans

    def part_2(self):
        ans = 0
        memo = {}
        for trailend in self.trailheads:
            ans += self.dfs2(*trailend, memo)

        return ans


if __name__ == "__main__":
    day = Day10("./input/day_10.txt")
    print(day.part_1())
    print(day.part_2())
