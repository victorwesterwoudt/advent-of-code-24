from __future__ import annotations

from enum import Enum
from functools import cached_property

from src import Day


def adv(self: Day17, op: int) -> int:
    return self.A / 2 ** self.combo(op)


def bxl(self: Day17, op: int) -> int:
    return self.A + self.combo(op)


class Instruction(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Day17(Day):
    def __init__(self, input):
        super().__init__(input)
        self.A, self.B, self.C, self.prog = self.data

    @cached_property
    def data(self):
        A = 0
        B = 0
        C = 0
        with open(self._input) as f:
            reg, prog = f.read().strip().split("\n\n")

        for r in reg.split("\n"):
            if "A" in r:
                A = int(r.split(": ")[1])
            elif "B" in r:
                B = int(r.split(": ")[1])
            elif "C" in r:
                C = int(r.split(": ")[1])

        prog = list(map(int, prog.split()[1].split(",")))

        return A, B, C, prog

    @staticmethod
    def combo(op: int, A, B, C) -> int:
        match op:
            case 0 | 1 | 2 | 3:
                return op
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                raise ValueError("Invalid operation")
            case _:
                raise ValueError("Unknown operation")

    def solve(self, A, B, C, prog):
        idx = 0
        output = []

        while True:
            if idx >= len(prog):
                break

            instruction = prog[idx]
            operand = prog[idx + 1]
            idx = idx + 2

            match Instruction(instruction):
                case Instruction.ADV:
                    A = int(A / 2 ** self.combo(operand, A, B, C))
                case Instruction.BXL:
                    B = B ^ operand
                case Instruction.BST:
                    B = self.combo(operand, A, B, C) % 8
                case Instruction.JNZ:
                    if A == 0:
                        continue
                    idx = operand
                case Instruction.BXC:
                    B = B ^ C
                case Instruction.OUT:
                    output.append(self.combo(operand, A, B, C) % 8)
                case Instruction.BDV:
                    B = int(A / 2 ** self.combo(operand, A, B, C))
                case Instruction.CDV:
                    C = int(A / 2 ** self.combo(operand, A, B, C))

        return output

    def part_1(self):
        return ",".join(
            map(str, self.solve(self.A, self.B, self.C, self.prog))
        )

    def part_2(self):
        A = 0
        step = 0
        while True:
            output = self.solve(A, self.B, self.C, self.prog)
            print(A, output)
            if output == self.prog:
                break

            if output == self.prog[-(step + 1) :]:
                A *= 8
                step += 1
            else:
                A += 1

        return A


if __name__ == "__main__":
    day = Day17("./input/day_17.txt")
    print(day.part_1())
    print(day.part_2())
