# https://atcoder.jp/contests/abc120/tasks/abc120_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, K = map(int, input().split())

    MAX_V = max(A, B)
    cd = set()
    for i in range(MAX_V, 0, -1):
        if A % i == 0 and B % i == 0:
            cd.add(i)
    print(sorted(cd, reverse=True)[K-1])

if __name__ == '__main__':
    main()
