# https://atcoder.jp/contests/abc119/tasks/abc119_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    BTC_RATE = 380000
    ans = 0
    for _ in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'BTC':
            x *= BTC_RATE
        ans += x
    print(ans)

if __name__ == '__main__':
    main()

