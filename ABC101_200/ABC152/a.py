# https://atcoder.jp/contests/abc152/tasks/abc152_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    if n == m:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
