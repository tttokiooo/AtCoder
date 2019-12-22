# https://atcoder.jp/contests/abc135/tasks/abc135_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = tuple(map(int, input().split()))

    ans = 0
    for i in range(n):
        ai = a[i]
        bi = b[i]
        if ai >= bi:
            ans += bi
        else:
            bi -= ai
            ans += ai

            aj = a[i+1]
            if aj >= bi:
                a[i+1] -= bi
                ans += bi
            else:
                a[i+1] = 0
                ans += aj
    print(ans)

if __name__ == '__main__':
    main()
