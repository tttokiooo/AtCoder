# https://atcoder.jp/contests/abc136/tasks/abc136_d
import sys
import math
import itertools
def input(): return sys.stdin.readline().rstrip()

def main():
    s = list(input())
    g = itertools.groupby(s)
    ans = []
    for key, group in g:
        if key == 'R':
            r = len(tuple(group))
            continue
        l = len(tuple(group))

        ans += [0] * (r-1) + [math.ceil(r/2) + math.floor(l/2)]
        ans += [math.floor(r/2) + math.ceil(l/2)] + [0] * (l-1)
    print(*ans)

if __name__ == '__main__':
    main()
