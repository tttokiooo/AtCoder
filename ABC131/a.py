# https://atcoder.jp/contests/abc131/tasks/abc131_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    s = input()
    pre = ''
    for i in list(s):
        if pre == i:
            print('Bad')
            break
        pre = i
    else:
        print('Good')

if __name__ == '__main__':
    main()
