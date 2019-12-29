# https://atcoder.jp/contests/abc149/tasks/abc149_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a-k, b)
    else:
        print(0, max(a+b-k, 0))

if __name__ == '__main__':
    main()
