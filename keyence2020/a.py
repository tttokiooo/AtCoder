# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    H = int(input())
    W = int(input())
    N = int(input())

    hw = max(H, W)
    print(math.ceil(N / hw))

if __name__ == '__main__':
    main()
