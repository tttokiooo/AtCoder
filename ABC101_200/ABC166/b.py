# https://atcoder.jp/contests/abc166/tasks/abc166_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    ans = [0] * N
    for _ in range(K):
        d = int(input())
        A = tuple(map(int, input().split()))
        for a in A:
            ans[a - 1] += 1
    print(len([a for a in ans if a == 0]))

if __name__ == '__main__':
    main()
