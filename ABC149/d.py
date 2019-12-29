# https://atcoder.jp/contests/abc149/tasks/abc149_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    pre = [None] * n

    ans = 0
    for i, j in enumerate(t):
        if i < k or j != pre[i-k]:
            pre[i] = j
            if j == 'r':
                ans += p
            elif j == 's':
                ans += r
            else:
                ans += s
    print(ans)

if __name__ == '__main__':
    main()
