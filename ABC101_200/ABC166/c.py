# https://atcoder.jp/contests/abc166/tasks/abc166_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    H = tuple(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    data = [[0] for _ in range(N)]
    for a, b in AB:
        data[a - 1].append(H[b - 1])
        data[b - 1].append(H[a - 1])

    ans = 0
    for i, h in enumerate(H):
        if h > max(data[i]):
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
