# https://atcoder.jp/contests/abc124/tasks/abc124_d
import sys
from collections import deque
from itertools import groupby
def input(): return sys.stdin.readline().rstrip()

def main():
    _, K = map(int, input().split())
    S = input()

    ans = 0
    l = 0
    que = deque()
    que_sum = 0
    for k, v in groupby(S):
        if k == '0':
            l0 = len(tuple(v))
            que_sum += l0
            que.append(l + l0)
            if len(que) > K:
                que_sum -= que.popleft()
        else:
            l = len(tuple(v))
            que_sum += l
        if que_sum > ans:
            ans = que_sum
    print(ans)

if __name__ == '__main__':
    main()
