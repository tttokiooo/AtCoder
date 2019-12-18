# https://atcoder.jp/contests/abc140/tasks/abc140_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    b = list(map(int, input().split()))
    b = [b[0]] + b + [b[-1]]
    print(sum([min(b[i], b[i+1]) for i in range(n)]))

if __name__ == '__main__':
    main()
