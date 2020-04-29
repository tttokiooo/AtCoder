# https://atcoder.jp/contests/abc161/tasks/abc161_d
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def main():
    K = int(input())
    if K <= 10:
        print(K)
        exit()

    q = deque(range(1, 10))
    K -= 9
    while q:
        v = q.popleft()
        sv = v % 10
        for i in (-1, 0, 1):
            if 0 <= sv + i < 10:
                if K == 1:
                    print(v * 10 + sv + i)
                    exit()
                K -= 1
                q.append(v * 10 + sv + i)

if __name__ == '__main__':
    main()
