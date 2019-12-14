# https://atcoder.jp/contests/abc143/tasks/abc143_c
import sys
input = sys.stdin.readline
import itertools

def main():
    input()
    print(len(tuple(itertools.groupby(input().rstrip()))))

if __name__ == '__main__':
    main()
