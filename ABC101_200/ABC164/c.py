# https://atcoder.jp/contests/abc164/tasks/abc164_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    print(len(set(s)))

if __name__ == '__main__':
    main()
