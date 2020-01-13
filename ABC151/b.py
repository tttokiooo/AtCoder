# https://atcoder.jp/contests/abc151/tasks/abc151_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k, m = map(int, input().split())
    a = [int(i) for i in input().split()]

    s = sum(a)
    ans = m * n - s
    if ans > k:
        print(-1)
    elif ans <= 0:
        print(0)
    else:
        print(ans)

if __name__ == '__main__':
    main()
