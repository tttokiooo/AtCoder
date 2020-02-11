# https://atcoder.jp/contests/abc136/tasks/abc136_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    h_ls = tuple(map(int, input().split()))
    h_ = h_ls[-1]

    for h in h_ls[-2::-1]:
        if h > h_:
            if h - 1 == h_:
                continue
            print('No')
            quit()
        h_ = h
    print('Yes')


if __name__ == '__main__':
    main()
