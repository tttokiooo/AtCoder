# https://atcoder.jp/contests/abc162/tasks/abc162_e
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    ans = 0
    memo = [0] * (K + 1)
    for i in range(K, 0, -1):
        c = pow(K // i, N, MOD) - sum(memo[i::i]) % MOD
        memo[i] = c
        ans += i * c
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()
