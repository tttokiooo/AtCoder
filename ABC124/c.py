# https://atcoder.jp/contests/abc124/tasks/abc124_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = tuple(map(int, tuple(input())))

    ans = 10 ** 5
    for i in range(2):
        v = i
        a = 0
        for s in S:
            if s != v:
                a += 1
            v = 1 if v == 0 else 0
        ans = min(ans, a)
    print(ans)

if __name__ == '__main__':
    main()
