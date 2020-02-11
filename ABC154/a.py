# https://atcoder.jp/contests/abc154/tasks/abc154_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        print(A-1, B)
    else:
        print(A, B-1)

if __name__ == '__main__':
    main()
