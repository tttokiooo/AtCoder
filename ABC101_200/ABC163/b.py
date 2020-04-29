# https://atcoder.jp/contests/abc163/tasks/abc163_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    A = tuple(map(int, input().split()))

    sum_A = sum(A)
    if sum_A > N:
        print(-1)
    else:
        print(N - sum_A)

if __name__ == '__main__':
    main()
