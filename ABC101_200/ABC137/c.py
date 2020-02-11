# https://atcoder.jp/contests/abc137/tasks/abc137_c
from collections import Counter
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    c = Counter([''.join(sorted(input())) for _ in range(n)]).values()
    print(sum([i * (i - 1) // 2 for i in c]))

if __name__ == '__main__':
    main()
