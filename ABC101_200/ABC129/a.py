# https://atcoder.jp/contests/abc129/tasks/abc129_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    pqr = sorted(map(int, input().split()))
    print(sum(pqr[:-1]))

if __name__ == '__main__':
    main()
