# https://atcoder.jp/contests/abc123/tasks/abc123_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    AtoE = [int(input()) for _ in range(5)]

    min_i = 0
    min_v = AtoE[min_i]
    for i, v in enumerate(AtoE):
        if min_v > v:
            min_i = i
            min_v = v
    
    ans = 0
    for i, v in enumerate(AtoE):
        if min_i == i:
            ans += (N + v - 1 ) // v
        else:
            ans += (min_v + v - 1) // v
    print(ans)

if __name__ == '__main__':
    main()
