# https://atcoder.jp/contests/abc112/tasks/abc112_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    if N == 1:
        print('Hello World')
    else:
        A = int(input())
        B = int(input())
        print(A + B)

if __name__ == '__main__':
    main()
