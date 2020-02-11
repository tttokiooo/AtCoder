# https://atcoder.jp/contests/abc153/tasks/abc153_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H = int(input())

    c = 0
    while H > 0:
        c += 1
        if H < 1:
            H = 0
        else:
            H //= 2
    print(sum([2 ** i for i in range(c)]))

if __name__ == '__main__':
    main()
