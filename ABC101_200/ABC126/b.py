# https://atcoder.jp/contests/abc126/tasks/abc126_b
import sys
def input(): return sys.stdin.readline().rstrip()

def is_month(n):
    return 1 <= n <= 12

def main():
    s = input()
    s1 = int(s[:2])
    s2 = int(s[2:])

    if is_month(s1) and is_month(s2):
        print('AMBIGUOUS')
    elif is_month(s1):
        print('MMYY')
    elif is_month(s2):
        print('YYMM')
    else:
        print('NA')

if __name__ == '__main__':
    main()

