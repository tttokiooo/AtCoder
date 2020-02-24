# https://atcoder.jp/contests/abc155/tasks/abc155_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b, c = map(int, input().split())
    if len(set([a,b,c])) == 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
