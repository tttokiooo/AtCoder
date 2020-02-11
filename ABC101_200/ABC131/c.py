# https://atcoder.jp/contests/abc131/tasks/abc131_c
import sys
import fractions
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b, c, d = map(int, input().split())
    cd_gcd = c * d // fractions.gcd(c, d)
    cnt = lambda n: n - n // c - n // d + n // cd_gcd
    print(cnt(b) - cnt(a-1))

if __name__ == '__main__':
    main()
