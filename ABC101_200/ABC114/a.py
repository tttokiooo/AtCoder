# https://atcoder.jp/contests/abc114/tasks/abc114_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    X = int(input())
    if X in (3, 5, 7):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
