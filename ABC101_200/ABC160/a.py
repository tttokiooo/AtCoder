# https://atcoder.jp/contests/abc160/tasks/abc160_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    if S[2] == S[3] and S[4] == S[5]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
