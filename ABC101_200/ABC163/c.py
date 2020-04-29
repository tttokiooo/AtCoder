# https://atcoder.jp/contests/abc163/tasks/abc163_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = tuple(map(int, input().split()))

    ans = [0] * (n + 1)
    for a in A:
        ans[a] += 1
    print(*ans[1:], sep='\n')

if __name__ == '__main__':
    main()
