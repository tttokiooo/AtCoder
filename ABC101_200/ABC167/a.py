# https://atcoder.jp/contests/abc167/tasks/abc167_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    T = input()

    sl = len(S)
    if S == T[:sl]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
