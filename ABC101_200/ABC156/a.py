# https://atcoder.jp/contests/abc156/tasks/abc156_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, R = map(int, input().split())
    if N < 10:
        R += 100 * (10 - N)
    print(R)

if __name__ == '__main__':
    main()
