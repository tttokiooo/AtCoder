# https://atcoder.jp/contests/abc104/tasks/abc104_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = list(input())

    isWA = False
    if S[0] != 'A':
        isWA = True

    if S[2:-1].count('C') != 1:
        isWA = True

    for s in S:
        if s == 'A' or s == 'C':
            continue
        if s.isupper():
            isWA = True

    if isWA:
        print('WA')
    else:
        print('AC')

if __name__ == '__main__':
    main()
