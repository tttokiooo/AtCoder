# https://atcoder.jp/contests/abc113/tasks/abc113_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = tuple(map(lambda h: abs(T - int(h) * 0.006 - A), input().split()))
    print(H.index(min(H)) + 1)

if __name__ == '__main__':
    main()
