# https://atcoder.jp/contests/abc159/tasks/abc159_d
import sys
from collections import Counter

def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    c = Counter(A)

    data = [0] * (N+1)
    sum_count = 0
    for i, v in c.items():
        if v < 2:
            continue
        value = v * (v - 1) // 2
        data[i] = value - value * (v - 2) // v
        sum_count += value

    print('\n'.join([str(sum_count - data[a]) for a in A]))

if __name__ == '__main__':
    main()
