# https://atcoder.jp/contests/abc109/tasks/abc109_c
import sys
from fractions import gcd
from functools import reduce
def input(): return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10 ** 9)
def main():
    _, X = input().split()
    x = sorted(map(int, input().split() + [X]))
    min_x = x[0]
    x = map(lambda a: a - min_x, x[1:])
    print(reduce(gcd, x))

if __name__ == '__main__':
    main()
