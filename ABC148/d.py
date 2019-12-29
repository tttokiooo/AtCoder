# https://atcoder.jp/contests/abc148/tasks/abc148_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == ans + 1:
            ans += 1
    if ans:
        print(n - ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()
