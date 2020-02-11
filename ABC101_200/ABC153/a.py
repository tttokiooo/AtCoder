# https://atcoder.jp/contests/abc153/tasks/abc153_a
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    H, A = map(int, input().split())
    print(math.ceil(H/A))

if __name__ == '__main__':
    main()
