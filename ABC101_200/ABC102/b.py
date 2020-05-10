# https://atcoder.jp/contests/abc102/tasks/abc102_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    print(max(A) - min(A))

if __name__ == '__main__':
    main()
