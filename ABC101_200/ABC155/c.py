# https://atcoder.jp/contests/abc155/tasks/abc155_c
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        d[input()] += 1
    max_v = max(d.values())
    d_sorted = sorted(d)

    for word in d_sorted:
        if d[word] == max_v:
            print(word)

if __name__ == '__main__':
    main()
