# https://atcoder.jp/contests/abc143/tasks/abc143_a
import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    print(max(a - 2 * b, 0))

if __name__ == '__main__':
    main()
