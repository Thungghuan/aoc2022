import argparse
import os
import importlib


def get_config():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="subcommand")

    new_puzzle = subparser.add_parser("new")
    new_puzzle.add_argument("day", type=int)

    run_solution = subparser.add_parser("run")
    run_solution.add_argument("day", type=int)
    run_solution.add_argument("-t", "--test", type=bool, default=False)

    return parser.parse_args()


def add_new_puzzle(day):
    day_directory = "days/d" + f"0{day}" if day < 10 else f"{day}"

    if not os.path.exists(day_directory):
        os.mkdir(day_directory)

    with open("templates/__init__.py", "r") as f:
        puzzle_codes = f.read()

    with open(os.path.join(day_directory, "__init__.py"), "w") as f:
        f.write(puzzle_codes)

    input_txt = os.path.join(day_directory, "input.txt")
    if not os.path.exists(input_txt):
        with open(os.path.join(day_directory, "input.txt"), "w") as f:
            f.write("")

    test_txt = os.path.join(day_directory, "test.txt")
    if not os.path.exists(test_txt):
        with open(os.path.join(day_directory, "test.txt"), "w") as f:
            f.write("")


def run_puzzle_code(day, test, part=0):
    format_day = f"d0{day}" if day < 10 else f"d{day}"
    day_directory = "days/" + format_day
    test_cases = "test.txt" if test else "input.txt"

    puzzle = importlib.import_module(f"days.{format_day}").Puzzle()
    puzzle.get_test_cases(os.path.join(day_directory, test_cases))

    if part == 0:
        puzzle.part1()
        puzzle.part2()
    elif part == 1:
        puzzle.part1()
    elif part == 2:
        puzzle.part2()


def main():
    config = get_config()

    if config.subcommand == "new":
        add_new_puzzle(config.day)
    elif config.subcommand == "run":
        run_puzzle_code(config.day, config.test)


if __name__ == "__main__":
    main()
