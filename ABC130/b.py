# https://atcoder.jp/contests/abc130/tasks/abc130_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, x = map(int, input().split())
    l = tuple(map(int, input().split()))

    d = 0
    for i in range(1, n+1):
        d += l[i-1]
        if d > x:
            print(i)
            quit()
    else:
        print(n+1)

if __name__ == '__main__':
    main()
