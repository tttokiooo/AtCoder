# https://atcoder.jp/contests/abc132/tasks/abc132_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    s = input()
    for i in set(s):
        if s.count(i) != 2:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()
