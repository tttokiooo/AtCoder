# https://atcoder.jp/contests/abc165/tasks/abc165_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M, Q = map(int, input().split())
    abcd = [tuple(map(int, input().split())) for _ in range(Q)]

    data = [[1]]
    for _ in range(N):
        tmp = []
        for d in data:
            v = d[-1]
            for m in range(M):
                if v + m > M:
                    break
                tmp.append(d + [v + m])
        data = tmp

    ans = 0
    for val in data:
        tmp_ans = 0
        for a, b, c, d in abcd:
            if val[b - 1] - val[a - 1] == c:
                tmp_ans += d
        if tmp_ans > ans:
            ans = tmp_ans
    print(ans)

if __name__ == '__main__':
    main()
