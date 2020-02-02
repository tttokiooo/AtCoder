# https://atcoder.jp/contests/abc120/tasks/abc120_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    print(len(S) - abs(S.count('1') - S.count('0')))

if __name__ == '__main__':
    main()
