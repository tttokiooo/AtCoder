# https://atcoder.jp/contests/abc130/tasks/abc130_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    x, a = map(int, input().split())
    print(0 if x < a else 10)

if __name__ == '__main__':
    main()
