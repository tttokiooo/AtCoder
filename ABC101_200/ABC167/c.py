# https://atcoder.jp/contests/abc167/tasks/abc167_c
import sys
from itertools import product
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M, X = map(int, input().split())
    CA = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    bit_list = list(product([0, 1], repeat=N))
    for bits in bit_list:
        tmp_ans = 0
        m_list = [0] * M

        for ca, bit in zip(CA, bits):
            if bit == 0:
                continue
            tmp_ans += ca[0]
            if ans > 0 and tmp_ans > ans:
                break
            for i, v in enumerate(ca[1:]):
                m_list[i] += v
        if min(m_list) >= X:
            if tmp_ans < ans or ans < 0:
                ans = tmp_ans
    print(ans)

if __name__ == '__main__':
    main()
