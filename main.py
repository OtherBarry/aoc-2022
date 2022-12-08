import argparse

from four import Problem4
from one import Problem1
from three import Problem3
from two import Problem2

PROBLEM_MAP = {
    1: Problem1,
    2: Problem2,
    3: Problem3,
    4: Problem4,
    # 5: Problem5,
    # 6: Problem6,
    # 7: Problem7,
    # 8: Problem8,
    # 9: Problem9,
    # 10: Problem10,
    # 11: Problem11,
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
    print("\nDone")