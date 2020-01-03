# https://atcoder.jp/contests/abc131/tasks/abc131_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab_sorted = sorted(ab, key=lambda x: x[1])

    sum_a = 0
    for a, b in ab_sorted:
        sum_a += a
        if b < sum_a:
            print('No')
            quit()
    print('Yes')

if __name__ == '__main__':
    main()
