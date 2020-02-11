# https://atcoder.jp/contests/abc145/tasks/abc145_c
import math
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    sum_v = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if i != j:
                sum_v += math.sqrt((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)
    print(sum_v * 2 / n)

if __name__ == '__main__':
    main()
