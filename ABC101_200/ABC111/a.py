# https://atcoder.jp/contests/abc111/tasks/abc111_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = input()
    conv = {'1': '9', '9': '1'}
    print(conv[n[0]] + conv[n[1]] + conv[n[2]])

if __name__ == '__main__':
    main()
