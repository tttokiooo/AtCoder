# https://atcoder.jp/contests/dp/tasks/dp_c
n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = abc[0]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abc[i][j])
print(max(dp[n - 1]))
