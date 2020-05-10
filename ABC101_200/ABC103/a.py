# https://atcoder.jp/contests/abc103/tasks/abc103_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A = sorted(map(int, input().split()))
    print(A[2] - A[0])

if __name__ == '__main__':
    main()
