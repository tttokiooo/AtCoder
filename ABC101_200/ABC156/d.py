# https://atcoder.jp/contests/abc156/tasks/abc156_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    MOD = 10 ** 9 + 7
    n, a, b = map(int, input().split())

    def comb_c(n, r):
        if r > n - r:
            r = n - r
        a, b = 1, 1
        for i in range(r):
            a = a * (n - i) % MOD
            b = b * (i + 1) % MOD
        return a * pow(b, MOD-2, MOD)

    ans = pow(2, n, MOD) - 1
    ans -= comb_c(n, a)
    ans -= comb_c(n, b)
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()
