import os


class BasePuzzle:
    lines = []
    mode = "normal"

    def __init__(self) -> None:
        pass

    def __init_puzzle__(self) -> None:
        pass

    def __init_part__(self) -> None:
        pass

    def set_mode(self, mode):
        self.mode = "test"

    def part1(self):
        pass

    def part2(self):
        pass

    def get_test_cases(self, filename):
        f = open(filename)

        self.raw = f.read().strip()
        self.lines = self.raw.split("\n")

        f.close()
