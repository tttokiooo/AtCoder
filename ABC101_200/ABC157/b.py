# https://atcoder.jp/contests/abc157/tasks/abc157_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A = [tuple(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]

    ans = [[[] for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j, a in enumerate(A[i]):
            ans[i][j] = a in B

    yes = []
    for i in range(3):
        yes.append(all(ans[i]))
        yes.append(all([ans[0][i], ans[1][i], ans[2][i]]))
    yes.append(all([ans[0][0], ans[1][1], ans[2][2]]))
    yes.append(all([ans[2][0], ans[1][1], ans[0][2]]))

    if any(yes):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
