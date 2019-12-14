# https://atcoder.jp/contests/abc141/tasks/abc141_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    s = input()
    if 'L' not in s[::2] and 'R' not in s[1::2]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
