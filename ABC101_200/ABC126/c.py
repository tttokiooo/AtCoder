# https://atcoder.jp/contests/abc126/tasks/abc126_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    s = 0
    while 2 ** s < k:
        s += 1

    ans = 0
    for i in range(1, n+1):
        c = 0
        while i < k:
            i *= 2
            c += 1
        ans += 2 ** (s - c)
    print(ans / ((2 ** s) * n))

if __name__ == '__main__':
    main()
