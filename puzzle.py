import os


class BasePuzzle:
    lines = []

    def __init__(self) -> None:
        pass

    def part1(self):
        pass

    def part2(self):
        pass

    def get_test_cases(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()
