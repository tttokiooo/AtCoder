# https://atcoder.jp/contests/abc128/tasks/abc128_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    s = [tuple(map(int, input().split()[1:])) for _ in range(m)]
    p = tuple(map(int, input().split()))

    c = 0
    f = '0' + str(n) + 'b'
    for i in range(2 ** n):
        xi = 'x' + format(i, f)
        for j in range(m):
            if sum([int(xi[k]) for k in s[j]]) % 2 != p[j]:
                break
        else:
            c += 1
    print(c)

if __name__ == '__main__':
    main()
