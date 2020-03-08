# https://atcoder.jp/contests/abc113/tasks/abc113_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    PY = [tuple(map(int, input().split())) for _ in range(M)]

    sorted_PY  = sorted(PY)

    ans = [{} for _ in range(N+1)]
    i = 0
    pre = sorted_PY[0][0]
    for p, y in sorted_PY:
        if pre != p:
            i = 0
        i += 1
        ans[p][y] = i
        pre = p

    for p, y in PY:
        print(str(p).zfill(6) + str(ans[p][y]).zfill(6))

if __name__ == '__main__':
    main()
