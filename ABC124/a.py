# https://atcoder.jp/contests/abc124/tasks/abc124_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())

    ans = 0
    for _ in range(2):
        if A > B:
            ans += A
            A -= 1
        else:
            ans += B
            B -= 1
    print(ans)

if __name__ == '__main__':
    main()
