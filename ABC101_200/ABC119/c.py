# https://atcoder.jp/contests/abc119/tasks/abc119_c
import sys
from itertools import product
def input(): return sys.stdin.readline().rstrip()

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]

    ans = 10 ** 7
    for l_li in product(range(4), repeat = N):
        cost = -30
        a = 0
        b = 0
        c = 0
        for i, li in enumerate(l_li):
            if li > 0:
                cost += 10
                if li == 1:
                    a += l[i]
                elif li == 2:
                    b += l[i]
                elif li == 3:
                    c += l[i]
        cost += abs(A - a) + abs(B - b) + abs(C - c)
        if a * b * c > 0 and ans > cost:
            ans = cost
    print(ans)

if __name__ == '__main__':
    main()

