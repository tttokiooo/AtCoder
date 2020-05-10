# https://atcoder.jp/contests/abc103/tasks/abc103_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    a = tuple(map(int, input().split()))

    print(sum(a) - len(a))

if __name__ == '__main__':
    main()
