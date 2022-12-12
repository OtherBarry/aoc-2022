import argparse
from timeit import default_timer as timer

from solutions.base import format_time
from solutions.day08 import Solution08
from solutions.day11 import Solution11
from solutions.day05 import Solution05
from solutions.day04 import Solution04
from solutions.day01 import Solution01
from solutions.day07 import Solution07
from solutions.day06 import Solution06
from solutions.day10 import Solution10
from solutions.day03 import Solution03
from solutions.day02 import Solution02

PROBLEM_MAP = {
    1: Solution01,
    2: Solution02,
    3: Solution03,
    4: Solution04,
    5: Solution05,
    6: Solution06,
    7: Solution07,
    8: Solution08,
    # 9: Problem9,
    10: Solution10,
    11: Solution11,
    # 12: Problem12,
    # 13: Problem13,
    # 14: Problem14,
    # 15: Problem15,
    # 16: Problem16,
    # 17: Problem17,
    # 18: Problem18,
    # 19: Problem19,
    # 20: Problem20,
    # 21: Problem21,
    # 22: Problem22,
    # 23: Problem23,
    # 24: Problem24,
    # 25: Problem25,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problems", nargs="*", type=int, help="The problems to run")
    args = parser.parse_args()
    print("Running problems")

    start = timer()
    if not args.problems:
        for day, problem_class in PROBLEM_MAP.items():
            print(f"\nProblem {day}:")
            problem = problem_class(f"inputs/{day}.txt")
            problem.run()
    else:
        for day in args.problems:
            print(f"\nProblem {day}:")
            problem = PROBLEM_MAP[day](f"inputs/{day}.txt")
            problem.run()
    end = timer()
    print(f"\nCompleted in {format_time(end - start)}")
