# https://atcoder.jp/contests/abc162/tasks/abc162_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    S = list(input())
    R = set()
    G = set()
    B = set()

    MIN_MAX = lambda a, b: (b, a) if a > b else (a, b)

    for i, s in enumerate(S):
        if s == 'R':
            R.add(i)
        elif s == 'G':
            G.add(i)
        else:
            B.add(i)

    b_len = len(B)
    ans = 0
    for r in R:
        for g in G:
            v1, v2 = MIN_MAX(r, g)
            rg_diff = v2 - v1
            ans += b_len
            if v2 + rg_diff in B:
                ans -= 1
            if v1 - rg_diff in B:
                ans -= 1
            if (r + g) % 2 == 0 and (r + g) // 2 in B:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
