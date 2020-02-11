# https://atcoder.jp/contests/abc127/tasks/abc127_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    r, d, x = map(int, input().split())

    for _ in range(10):
        x = r * x - d
        print(x)
if __name__ == '__main__':
    main()
