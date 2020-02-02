# https://atcoder.jp/contests/abc121/tasks/abc121_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, _, C = map(int, input().split())
    B = tuple(map(int, input().split()))

    ans = 0
    for _ in range(N):
        A = map(int, input().split())
        if sum([i * j for i, j in zip(A, B)]) + C > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
