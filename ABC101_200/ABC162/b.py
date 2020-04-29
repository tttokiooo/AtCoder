# https://atcoder.jp/contests/abc162/tasks/abc162_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    print(sum([i for i in range(1, N + 1) if i % 3 != 0 and i % 5 != 0]))

if __name__ == '__main__':
    main()
