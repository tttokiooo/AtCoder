# https://atcoder.jp/contests/abc134/tasks/abc134_b
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    n, d = map(int, input().split())
    print(math.ceil(n / (2 * d + 1)))

if __name__ == '__main__':
    main()
