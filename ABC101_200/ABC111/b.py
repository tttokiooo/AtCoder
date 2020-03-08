# https://atcoder.jp/contests/abc111/tasks/abc111_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = input()
    rep = int('1' * len(N))
    ans = rep
    while ans < int(N):
        ans += rep
    print(ans)

if __name__ == '__main__':
    main()
