# https://atcoder.jp/contests/abc156/tasks/abc156_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    ans = 0
    while N >= 1:
        N //= K
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
