# https://atcoder.jp/contests/abc125/tasks/abc125_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    V = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))

    ans = 0
    for v, c in zip(V, C):
        ans += max(v-c, 0)
    print(ans)

if __name__ == '__main__':
    main()
