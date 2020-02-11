# https://atcoder.jp/contests/abc138/tasks/abc138_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a_tuple = tuple(map(int, input().split()))
    print(1 / sum([1 / a for a in a_tuple]))

if __name__ == '__main__':
    main()
