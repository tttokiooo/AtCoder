# https://atcoder.jp/contests/abc103/tasks/abc103_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    T = input()

    for _ in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()
