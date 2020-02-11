# https://atcoder.jp/contests/abc121/tasks/abc121_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())

    ans = 0
    for i in (A - 1, B):
        if i % 4 == 0:
            ans ^= i
        elif i % 2 == 0:
            ans ^= i ^ 1
        elif (i + 1) % 4 != 0:
            ans ^= 1
    print(ans)

if __name__ == '__main__':
    main()
