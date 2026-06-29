import sys
import numpy as np
from typing import List

def fun_format(filename : str) -> List[List[int]]:
    # open file
    with open(filename, 'r') as f:
        lines = f.readlines()
    # construct puzzle
    puzzle = []
    for line in lines:
        line2 = line.replace('\n', '').split()
        line_of_ints = [int(a) for a in line2]
        puzzle.append(line_of_ints)
    return puzzle

def classify(report : List[int]) -> str:
    """Classify a report as Safe or Unsafe"""
    # create vectors to check against safe list
    arr = np.array(report)
    diff_arr = np.diff(arr)
    # safe lists
    good_negative = [int(a) for a in [-1, -2, -3]]
    good_positive = [int(a) for a in [1, 2, 3]]
    # check against safe list
    if all([a in good_negative for a in diff_arr]):
        return 'Safe'
    if all([a in good_positive for a in diff_arr]):
        return 'Safe'
    return 'Unsafe'

def fun_safecount(puzzle : List[List[int]]) -> List[str]:
    """Count safe reports in a puzzle"""
    classifications = [fun_classify(x) for x in puzzle]
    return sum([c=='Safe' for c in classifications])

if __name__ == "__main__":
    puzzle = fun_format(sys.argv[1])
    safecount = 0
    for report in puzzle:
        report_class = classify(report)
        print('{} is {}'.format(report, report_class))
        if report_class=='Safe':
            safecount += 1
    print('there are {} safe reports in this puzzle'.format(safecount))
