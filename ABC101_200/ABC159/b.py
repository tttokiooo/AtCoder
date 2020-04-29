# https://atcoder.jp/contests/abc159/tasks/abc159_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    N = len(S)

    isKaibun = lambda s: s == s[::-1]
    if isKaibun(S) and isKaibun(S[:N//2]) and isKaibun(S[(N+1)//2:]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
