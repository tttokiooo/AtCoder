import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def main():
    H, W = map(int, input().split())
    S = [['#'] * (W+2)] + [['#'] + list(input()) + ['#'] for _ in range(H)] + [['#'] * (W+2)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    ans = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if S[i][j] == '#':
                continue
            init = (i, j)
            que = deque()
            que.append(init)
            dist = [[-1 for _ in range(W+2)] for _ in range(H+2)]
            dist[i][j] = 0

            while que:
                qh, qw = que.popleft()
                for dh, dw in direction:
                    h = qh + dh
                    w = qw + dw
                    if S[h][w] == '#' or dist[h][w] >= 0:
                        continue
                    dist[h][w] = dist[qh][qw] + 1
                    que.append((h, w))
            ans = max(ans, max([max(i) for i in dist]))
    print(ans)

if __name__ == '__main__':
    main()
