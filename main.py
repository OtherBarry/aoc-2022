import argparse

from one import Problem1
from three import Problem3
from two import Problem2

PROBLEM_MAP = {
    1: Problem1,
    2: Problem2,
    3: Problem3,
    # 4: ProblemFour,
    # 5: ProblemFive,
    # 6: ProblemSix,
    # 7: ProblemSeven,
    # 8: ProblemEight,
    # 9: ProblemNine,
    # 10: ProblemTen,
    # 11: ProblemEleven,
    # 12: ProblemTwelve,
    # 13: ProblemThirteen,
    # 14: ProblemFourteen,
    # 15: ProblemFifteen,
    # 16: ProblemSixteen,
    # 17: ProblemSeventeen,
    # 18: ProblemEighteen,
    # 19: ProblemNineteen,
    # 20: ProblemTwenty,
    # 21: ProblemTwentyOne,
    # 22: ProblemTwentyTwo,
    # 23: ProblemTwentyThree,
    # 24: ProblemTwentyFour,
    # 25: ProblemTwentyFive,
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
