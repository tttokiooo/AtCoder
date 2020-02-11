# https://atcoder.jp/contests/abc154/tasks/abc154_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = tuple(map(int, input().split()))
    if len(set(A)) == len(A):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
