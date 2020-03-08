# https://atcoder.jp/contests/abc158/tasks/abc158_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, A, B = map(int, input().split())
    full = N // (A+B)
    ans = full * A
    N -= full * (A+B)
    if N >= A:
        ans += A
    else:
        ans += N
    print(ans)

if __name__ == '__main__':
    main()
