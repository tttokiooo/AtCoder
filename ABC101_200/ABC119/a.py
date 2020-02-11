# https://atcoder.jp/contests/abc119/tasks/abc119_a
import sys
import datetime
def input(): return sys.stdin.readline().rstrip()

def main():
    Y, M, D = map(int, input().split('/'))
    if datetime.date(Y, M, D) <= datetime.date(2019, 4, 30):
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()

