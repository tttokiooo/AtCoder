# https://atcoder.jp/contests/abc130/tasks/abc130_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, int(W / 2 == x and H / 2 == y))

if __name__ == '__main__':
    main()
