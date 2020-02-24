# https://atcoder.jp/contests/abc156/tasks/abc156_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    X = tuple(map(int, input().split()))

    ans = 10000000
    for i in range(101):
        s = 0
        for x in X:
            s += (x - i) ** 2
        if ans > s:
            ans = s
    print(ans)

if __name__ == '__main__':
    main()
