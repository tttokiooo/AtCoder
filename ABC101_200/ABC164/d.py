# https://atcoder.jp/contests/abc164/tasks/abc164_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    s_list = list(map(int, list(S)))[::-1]
    MOD = 2019

    sum_v = 0
    cnt = [0] * MOD
    cnt[0] = 1
    for i, s in enumerate(s_list):
        sum_v += s * pow(10, i, MOD)
        sum_v %= MOD
        cnt[sum_v] += 1
    print(sum([c * (c - 1) // 2 for c in cnt if c > 1]))

if __name__ == '__main__':
    main()
