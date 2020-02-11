# https://atcoder.jp/contests/abc129/tasks/abc129_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    MOD = 1000000007
    n, m = map(int, input().split())
    a = {int(input()) for _ in range(m)}

    dp = [0] * (n+1)
    dp[:2] = 1, 1 if 1 not in a else 0

    for i in range(2, n+1):
        if i not in a:
            dp[i] += (dp[i-1] + dp[i-2]) % MOD
    print(dp[-1])

if __name__ == '__main__':
    main()
