# https://atcoder.jp/contests/abc136/tasks/abc136_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b, c = map(int, input().split())
    print(max(c - a + b, 0))

if __name__ == '__main__':
    main()
