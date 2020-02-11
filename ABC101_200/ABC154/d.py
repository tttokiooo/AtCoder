# https://atcoder.jp/contests/abc154/tasks/abc154_d
import sys
from itertools import accumulate
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    P = tuple(map(int, input().split()))

    sum_ls = tuple(accumulate(range(max(P) + 1)))
    acc_P = [0] + list(accumulate([sum_ls[p] / p for p in P]))

    ans = 0
    for i in range(N - K + 1):
        v = acc_P[i+K] - acc_P[i]
        if v > ans:
            ans = v
    print(ans)

if __name__ == '__main__':
    main()
