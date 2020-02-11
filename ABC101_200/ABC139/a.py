# https://atcoder.jp/contests/abc139/tasks/abc139_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    s, t = input(), input()
    print(sum([1 for i in range(3) if s[i] == t[i]]))

if __name__ == '__main__':
    main()
