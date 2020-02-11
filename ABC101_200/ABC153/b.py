# https://atcoder.jp/contests/abc153/tasks/abc153_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H, N = map(int, input().split())
    A = tuple(map(int, input().split()))
    if sum(A) >= H:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
