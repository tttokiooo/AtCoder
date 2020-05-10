# https://atcoder.jp/contests/abc106/tasks/abc106_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ans = 0
    for i in range(105, n + 1, 2):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 8:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
