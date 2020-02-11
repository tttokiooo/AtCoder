# https://atcoder.jp/contests/abc147/tasks/abc147_b
from collections import deque
import sys
input = sys.stdin.readline

def main():
    d = deque(list(input().strip('\n')))
    c = 0
    while len(d) > 1:
        if d.popleft() != d.pop():
            c += 1
    print(c)

if __name__ == '__main__':
    main()
