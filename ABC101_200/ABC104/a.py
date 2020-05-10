# https://atcoder.jp/contests/abc104/tasks/abc104_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    R = int(input())
    if R < 1200:
        print('ABC')
    elif R < 2800:
        print('ARC')
    else:
        print('AGC')

if __name__ == '__main__':
    main()
