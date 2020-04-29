# https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    l = len(S)
    if l % 2 != 0:
        print('No')
    elif S.count('hi') == l // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
