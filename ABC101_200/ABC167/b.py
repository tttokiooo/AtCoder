# https://atcoder.jp/contests/abc167/tasks/abc167_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, C, K = map(int, input().split())

    ans = 0
    if A >= K:
        print(K)
        exit()
    ans += A
    K -= A
    if B >= K:
        print(ans)
        exit()
    K -= B
    if C >= K:
        ans -= K
    else:
        ans -= C
    print(ans)

if __name__ == '__main__':
    main()
