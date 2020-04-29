# https://atcoder.jp/contests/abc164/tasks/abc164_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()
