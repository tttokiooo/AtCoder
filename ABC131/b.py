# https://atcoder.jp/contests/abc131/tasks/abc131_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, l = map(int, input().split())

    ls = [i + l for i in range(n)]
    if l >= 0:
        ls = ls[1:]
    elif n + l - 1 < 0:
        ls = ls[:-1]

    print(sum(ls))

if __name__ == '__main__':
    main()
