# https://atcoder.jp/contests/abc120/tasks/abc120_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, C = map(int, input().split())
    print(min(C, B // A))

if __name__ == '__main__':
    main()
