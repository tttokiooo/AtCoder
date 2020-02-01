# https://atcoder.jp/contests/abc123/tasks/abc123_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    menu = [int(input()) for _ in range(5)]

    ans = 0
    min_m = 10
    for m in menu:
        ans += (m + 9) // 10 * 10
        if m % 10 > 0:
            min_m = min(min_m, m % 10)
    if min_m > 0:
        ans += min_m - 10
    print(ans)

if __name__ == '__main__':
    main()
