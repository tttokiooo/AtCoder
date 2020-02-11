# https://atcoder.jp/contests/abc133/tasks/abc133_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

if __name__ == '__main__':
    main()
