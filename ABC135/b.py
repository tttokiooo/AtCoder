# https://atcoder.jp/contests/abc135/tasks/abc135_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    p = list(map(int, input().split()))

    c = 0
    for i, v in enumerate(p):
        if (i + 1) != v:
            c += 1
        if c > 2:
            print('NO')
            quit()
    print('YES')

if __name__ == '__main__':
    main()
