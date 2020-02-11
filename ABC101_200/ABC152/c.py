# https://atcoder.jp/contests/abc152/tasks/abc152_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    P = map(int, input().split())

    min = 2 * (10 ** 5) + 10
    c = 0
    for i in P:
        if i <= min:
            c += 1
            min = i
    print(c)

if __name__ == '__main__':
    main()
