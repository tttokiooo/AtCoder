# https://atcoder.jp/contests/abc139/tasks/abc139_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    h = map(int, input().split())

    ans, bef, cnt = 0, 0, 0

    for i in h:
        if i <= bef:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
        bef = i
    print(max(ans, cnt))

if __name__ == '__main__':
    main()
