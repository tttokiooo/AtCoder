# https://atcoder.jp/contests/abc144/tasks/abc144_b
import math
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print('Yes')
            return None
    print('No')
if __name__ == '__main__':
    main()
