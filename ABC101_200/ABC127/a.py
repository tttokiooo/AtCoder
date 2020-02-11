# https://atcoder.jp/contests/abc127/tasks/abc127_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 12 >= a >=6:
        print(b // 2)
    else:
        print(0)

if __name__ == '__main__':
    main()
