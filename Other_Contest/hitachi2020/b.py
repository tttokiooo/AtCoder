# https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _, _, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    xyc = [list(map(int, input().split())) for _ in range(M)]

    ans = min(a) + min(b)
    for x, y, c in xyc:
        new = a[x - 1] + b[y - 1] - c
        if ans > new:
            ans = new
    print(ans)

if __name__ == '__main__':
    main()
