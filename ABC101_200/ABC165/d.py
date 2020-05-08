# https://atcoder.jp/contests/abc165/tasks/abc165_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, N = map(int, input().split())

    ans = -1
    for x in [N, B * (N // B) - 1]:
        if x >= 0:
            ans = max(ans, A * x // B - A * (x // B))
    print(ans)

if __name__ == '__main__':
    main()
