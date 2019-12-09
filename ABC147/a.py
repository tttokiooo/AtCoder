# https://atcoder.jp/contests/abc147/tasks/abc147_a
import sys
input = sys.stdin.readline

def main():
    if sum(map(int,input().split())) >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()
