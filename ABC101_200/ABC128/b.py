# https://atcoder.jp/contests/abc128/tasks/abc128_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    sp = [input().split() + [i+1] for i in range(n)]
    sp = sorted(sp, key=lambda x: (x[0], -int(x[1])))
    for _, _, i in sp:
        print(i)

if __name__ == '__main__':
    main()
