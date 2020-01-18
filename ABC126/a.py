# https://atcoder.jp/contests/abc126/tasks/abc126_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _, k = map(int, input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

if __name__ == '__main__':
    main()
