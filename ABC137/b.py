# https://atcoder.jp/contests/abc137/tasks/abc137_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    k, x = map(int, input().split())
    ans = [x]
    for i in range(1, k):
        ans.append(x+i)
        ans.append(x-i)
    ans = filter(lambda x: -1000000 <= x <= 1000000, ans)
    print(*sorted(ans))

if __name__ == '__main__':
    main()
