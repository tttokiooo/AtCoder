# https://atcoder.jp/contests/abc148/tasks/abc148_c
import sys
import fractions
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b= map(int, input().split())
    print(a * b // fractions.gcd(a, b))

if __name__ == '__main__':
    main()
