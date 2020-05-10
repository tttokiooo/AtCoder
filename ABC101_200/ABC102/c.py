# https://atcoder.jp/contests/abc102/tasks/abc102_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = map(int, input().split())
    A = sorted([a - i - 1 for i, a in enumerate(A)])

    b = A[N // 2]
    print(sum([abs(a - b) for a in A]))

if __name__ == '__main__':
    main()
