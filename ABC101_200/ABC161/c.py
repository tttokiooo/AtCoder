# https://atcoder.jp/contests/abc161/tasks/abc161_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())

    if N % K == 0:
        print(0)
    else:
        i = N // K
        print(min(abs(N - i * K), abs(N - (i+1) * K)))

if __name__ == '__main__':
    main()
