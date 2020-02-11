# https://atcoder.jp/contests/abc141/tasks/abc141_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    s = input()
    if s == 'Sunny':
        print('Cloudy')
    elif s == 'Cloudy':
        print('Rainy')
    elif s == 'Rainy':
        print('Sunny')

if __name__ == '__main__':
    main()
