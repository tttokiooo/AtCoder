# https://atcoder.jp/contests/abc142/tasks/abc142_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [None] * n
    for i, j in enumerate(a):
        ans[j-1] = i + 1
    print(*ans)

if __name__ == '__main__':
    main()
