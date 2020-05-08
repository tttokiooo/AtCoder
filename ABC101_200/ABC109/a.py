# https://atcoder.jp/contests/abc109/tasks/abc109_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())
    if A * B % 2 == 0:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
