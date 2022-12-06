import os


class BasePuzzle:
    lines = []

    def __init__(self) -> None:
        pass

    def __init_part__(self) -> None:
        pass

    def part1(self):
        pass

    def part2(self):
        pass

    def get_test_cases(self, filename):
        f = open(filename)

        self.raw = f.read()
        self.lines = self.raw.split("\n")

        f.close()
