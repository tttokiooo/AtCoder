# https://atcoder.jp/contests/abc122/tasks/abc122_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    ACGT = set(['A', 'C', 'G', 'T'])

    c = 0
    ans = 0
    for s in list(S):
        if s in ACGT:
            c += 1
        else:
            ans = max(ans, c)
            c = 0
    print(max(ans, c))

if __name__ == '__main__':
    main()
