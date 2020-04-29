# https://atcoder.jp/contests/abc162/tasks/abc162_c
import sys
from math import gcd
def input(): return sys.stdin.readline().rstrip()

def main():
    K = int(input())
    ans = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            ij = gcd(i, j)
            for k in range(1, K + 1):
                ans += gcd(ij, k)
    print(ans)

if __name__ == '__main__':
    main()
