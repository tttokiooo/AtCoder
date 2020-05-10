# https://atcoder.jp/contests/abc106/tasks/abc106_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())
    print(A * B - A - B + 1)

if __name__ == '__main__':
    main()
