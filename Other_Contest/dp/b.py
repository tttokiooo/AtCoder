# https://atcoder.jp/contests/dp/tasks/dp_b
n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [10 ** 9] * n
dp[0] = 0

for i in range(1, n):
    k_max = min(i, k)
    for j in range(1, k_max+1):
        dp[i] = min(dp[i], abs(h[i] - h[i-j]) + dp[i-j])
print(dp[n-1])
