# https://atcoder.jp/contests/abc118/tasks/abc118_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())

    ans = set(range(1, M+1))
    for _ in range(N):
        ans &= set(map(int, input().split()[1:]))
    print(len(ans))
    
if __name__ == '__main__':
    main()
