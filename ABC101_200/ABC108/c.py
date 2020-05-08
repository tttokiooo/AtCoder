# https://atcoder.jp/contests/abc108/tasks/abc108_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    ans = (N // K) ** 3

    if K % 2 == 0:
        k2 = K // 2
        ans += (1 + (N - k2) // K) ** 3
    print(ans)

if __name__ == '__main__':
    main()
