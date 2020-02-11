# https://atcoder.jp/contests/abc145/tasks/abc145_d
import math
import sys
input = sys.stdin.readline

def main():
    mod = 10 ** 9 + 7
    x, y = map(int, input().split())
    if (2 * y - x) % 3 != 0:
        print(0)
        return None

    n = (2 * y - x) // 3
    m = y - 2 * n

    if n < 0 or m < 0:
        print(0)
    elif n == 0 and m == 0:
        print(0)
    elif n == 0 or m == 0:
        print(1)
    else:
        s = n + m + 1
        f = [1] * s

        for i in range(1, s):
            f[i] = f[i-1] * i % mod

        ans = f[n+m]
        ans = ans * modinv(f[n]) % mod
        ans = ans * modinv(f[m]) % mod
        print(ans)

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

if __name__ == '__main__':
    main()
