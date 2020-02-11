# https://atcoder.jp/contests/abc118/tasks/abc118_c
import sys
def input(): return sys.stdin.readline().rstrip()

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def main():
    _ = int(input())
    A = tuple(map(int, input().split()))

    ans = A[0]
    for a in A[1:]:
        ans = gcd(ans, a)
    print(ans)
    
if __name__ == '__main__':
    main()
