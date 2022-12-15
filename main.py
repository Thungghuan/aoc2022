import argparse
import os
import importlib


def get_config():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="subcommand")

    new_puzzle = subparser.add_parser("new")
    new_puzzle.add_argument("day", type=int)
    new_puzzle.add_argument("--no-fetch", action="store_true")
    new_puzzle.add_argument("-r", "--recreate", action="store_true")

    run_solution = subparser.add_parser("run")
    run_solution.add_argument("day", type=int)
    run_solution.add_argument("-t", "--test", action="store_true")
    run_solution.add_argument("-p", "--part", type=int, default=0, choices=[0, 1, 2])

    return parser.parse_args()


def add_new_puzzle(day, no_fetch, recreate):
    if not os.path.exists("days"):
        os.mkdir("days")

    day_directory = "days/d" + (f"0{day}" if day < 10 else f"{day}")

    if not os.path.exists(day_directory):
        os.mkdir(day_directory)

    with open("templates/__init__.py", "r") as f:
        puzzle_codes = f.read()

    puzzle_path = os.path.join(day_directory, "__init__.py")
    if not os.path.exists(puzzle_path) or recreate:
        with open(puzzle_path, "w") as f:
            f.write(puzzle_codes)

    else:
        print(f"File {puzzle_path} already exists.")
        return

    if not no_fetch:
        with open(".cookie") as f:
            cookie = f.read()

        import requests

        test_case = requests.get(
            f"https://adventofcode.com/2022/day/{day}/input", headers={"Cookie": cookie}
        ).text

    input_txt = os.path.join(day_directory, "input.txt")
    if not os.path.exists(input_txt) or recreate:
        with open(os.path.join(day_directory, "input.txt"), "w") as f:
            if not no_fetch:
                f.write(test_case)

    test_txt = os.path.join(day_directory, "test.txt")
    if not os.path.exists(test_txt) or recreate:
        with open(os.path.join(day_directory, "test.txt"), "w") as f:
            f.write("")


def run_puzzle_code(day, test, part=0):
    format_day = f"d0{day}" if day < 10 else f"d{day}"
    day_directory = "days/" + format_day
    test_cases = "test.txt" if test else "input.txt"

    puzzle = importlib.import_module(f"days.{format_day}").Puzzle()
    puzzle.get_test_cases(os.path.join(day_directory, test_cases))
    puzzle.__init_puzzle__()
    puzzle.__init_part__()

    if test:
        puzzle.set_mode("test")

    if part == 0:
        puzzle.set_part(1)
        puzzle.part1()
        puzzle.__init_part__()
        puzzle.set_part(2)
        puzzle.part2()
    elif part == 1:
        puzzle.set_part(1)
        puzzle.part1()
    elif part == 2:
        puzzle.set_part(2)
        puzzle.part2()


def main():
    config = get_config()

    if config.subcommand == "new":
        add_new_puzzle(config.day, config.no_fetch, config.recreate)
    elif config.subcommand == "run":
        run_puzzle_code(config.day, config.test, config.part)


if __name__ == "__main__":
    main()
