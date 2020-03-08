# https://atcoder.jp/contests/abc112/tasks/abc112_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, T = map(int, input().split())
    MAX_ANS = 10000
    ans = MAX_ANS
    for _ in range(N):
        c, t = map(int, input().split())
        if c < ans and t <= T:
            ans = c
    if ans == MAX_ANS:
        print('TLE')
    else:
        print(ans)

if __name__ == '__main__':
    main()
