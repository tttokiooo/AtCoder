# https://atcoder.jp/contests/abc121/tasks/abc121_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0])

    ans = 0
    for a, b in AB:
        if M > b:
            M -= b
            ans += a * b
        else:
            ans += a * M
            print(ans)
            exit()

if __name__ == '__main__':
    main()
