# https://atcoder.jp/contests/abc165/tasks/abc165_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    X = int(input())

    ans = 0
    v = 100
    while True:
        ans += 1
        v = int(v * 1.01)
        if v >= X:
            print(ans)
            exit()

if __name__ == '__main__':
    main()
