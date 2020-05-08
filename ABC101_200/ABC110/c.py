# https://atcoder.jp/contests/abc110/tasks/abc110_c
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

def main():
    S = list(input())
    T = list(input())

    S_memo = defaultdict(str)
    T_memo = defaultdict(str)

    for s, t in zip(S, T):
        if (S_memo[s] and S_memo[s] != t) or (T_memo[t] and T_memo[t] != s):
            print('No')
            exit()
        else:
            S_memo[s] = t
            T_memo[t] = s
    print('Yes')

if __name__ == '__main__':
    main()
