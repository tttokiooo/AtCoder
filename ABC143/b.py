# https://atcoder.jp/contests/abc143/tasks/abc143_b
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    t = tuple(map(int, input().split()))
    print(sum([t[i] * t[j] for i in range(n) for j in range(i+1, n)]))

if __name__ == '__main__':
    main()
