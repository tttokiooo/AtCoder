# https://atcoder.jp/contests/abc152/tasks/abc152_e
import sys
from fractions import gcd
from functools import reduce
def input(): return sys.stdin.readline().rstrip()

def main():
    MOD = 10 ** 9 + 7
    n = int(input())
    A = tuple(map(int, input().split()))
    gcd_v = reduce(lcm, A)

    ans = 0
    for i in A:
        ans += gcd_v * pow(i, MOD-2, MOD) % MOD
        ans %= MOD
    print(ans)

def lcm(n, m):
    return (n * m) // gcd(n, m)    

if __name__ == '__main__':
    main()
