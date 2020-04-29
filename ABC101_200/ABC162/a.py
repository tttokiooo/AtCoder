# https://atcoder.jp/contests/abc162/tasks/abc162_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = input()
    if n.count('7') > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
