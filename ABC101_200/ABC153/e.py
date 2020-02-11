# https://atcoder.jp/contests/abc153/tasks/abc153_e
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [10**9+1] * (H+1)
    dp[0] = 0
    for a, b in AB:
        for i in range(1, H+1):
            if i - a >= 0:
                v = dp[i-a] + b
            else:
                v = b
            if dp[i] > v:
                dp[i] = v

    print(dp[H])

if __name__ == '__main__':
    main()
