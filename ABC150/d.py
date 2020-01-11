# https://atcoder.jp/contests/abc150/tasks/abc150_d
import sys
from fractions import gcd
from functools import reduce

def input(): return sys.stdin.readline().rstrip()

def div2_cnt(n):
    m = n
    c = 0
    while m % 2 == 0:
        m /= 2
        c += 1
    return c

def lcm(n, m):
    return (n * m) // gcd(n, m)

def main():
    _, m = map(int, input().split())
    a = [int(i) // 2 for i in set(input().split())]

    a0_c = div2_cnt(a[0])
    for i in a[1:]:
        if a0_c != div2_cnt(i):
            print(0)
            exit()

    first = reduce(lcm, a)
    if m < first:
        print(0)
    else:
        print((m - first) // first // 2 + 1)


if __name__ == '__main__':
    main()
