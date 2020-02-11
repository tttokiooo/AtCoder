# https://atcoder.jp/contests/abc127/tasks/abc127_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _, m = map(int, input().split())

    max = -1
    min = 10 ** 5 + 1
    for _ in range(m):
        l, r = map(int, input().split())
        if l > max:
            max = l
        if r < min:
            min = r
    if min - max < 0:
        print(0)
    else:
        print(min - max + 1)

if __name__ == '__main__':
    main()
