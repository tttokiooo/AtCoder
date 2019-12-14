# https://atcoder.jp/contests/abc144/tasks/abc144_c
import math
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a_max = int(math.sqrt(n))
    min_v = 10 ** 12
    for a in range(1, a_max+1):
        if n % a == 0:
            min_v = min(min_v, a + (n//a) - 2)
    print(min_v)

if __name__ == '__main__':
    main()
