# https://atcoder.jp/contests/abc142/tasks/abc142_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _, k = map(int, input().split())
    print(len([None for i in input().split() if int(i) >= k]))

if __name__ == '__main__':
    main()
