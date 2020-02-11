# https://atcoder.jp/contests/abc142/tasks/abc142_a
import math
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    print(math.ceil(n/2)/n)

if __name__ == '__main__':
    main()
