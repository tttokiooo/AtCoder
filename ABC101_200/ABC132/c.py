# https://atcoder.jp/contests/abc132/tasks/abc132_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    d1, d2 = sorted(map(int, input().split()))[n//2-1:n//2+1]
    print(d2 - d1)

if __name__ == '__main__':
    main()
