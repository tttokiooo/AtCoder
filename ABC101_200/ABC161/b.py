# https://atcoder.jp/contests/abc161/tasks/abc161_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))[::-1]

    if A[M - 1] * 4 * M >= sum(A):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
