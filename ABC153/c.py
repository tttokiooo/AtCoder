# https://atcoder.jp/contests/abc153/tasks/abc153_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    H = sorted(map(int, input().split()))
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

if __name__ == '__main__':
    main()
