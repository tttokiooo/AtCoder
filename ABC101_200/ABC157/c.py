# https://atcoder.jp/contests/abc157/tasks/abc157_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    sc = [tuple(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for i in range(N):
        for s, c in sc:
            if s == i + 1:
                if ans[i] == -1:
                    ans[i] = c
                else:
                    if ans[i] == c:
                        continue
                    else:
                        print(-1)
                        exit()
                
        if ans[i] == -1:
            if i == 0 and N > 1:
                ans[i] = 1
            else:
                ans[i] = 0
    ans_v = int(''.join(map(str, ans)))
    if len(str(ans_v)) == N:
        print(ans_v)
    else:
        print(-1)

if __name__ == '__main__':
    main()
