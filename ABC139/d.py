# https://atcoder.jp/contests/abc139/tasks/abc139_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    print((n-1) * n // 2)

if __name__ == '__main__':
    main()
