# https://atcoder.jp/contests/abc133/tasks/abc133_b
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    n, d = map(int, input().split())
    x = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0
    for ix, i in enumerate(x):
        for j in x[ix+1:]:
            if math.sqrt(sum([(i[k]-j[k]) ** 2 for k in range(d)])).is_integer():
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
