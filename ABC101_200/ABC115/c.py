# https://atcoder.jp/contests/abc115/tasks/abc115_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)], reverse=True)
    print(min([a - b for a, b in zip(H[:N-K+1], H[K-1:])]))

if __name__ == '__main__':
    main()
