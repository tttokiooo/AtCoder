# https://atcoder.jp/contests/abc105/tasks/abc105_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())

    if N == 0:
        print(0)
        exit()

    ans = []
    while N != 0:
        r = N % 2
        if r < 0:
            r += 2
        ans.append(r)
        N -= r
        N //= -2
    print("".join(map(str, ans[::-1])))

if __name__ == '__main__':
    main()
