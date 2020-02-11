# https://atcoder.jp/contests/abc117/tasks/abc117_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N, _ = map(int, input().split())
    X = sorted(map(int, input().split()))

    diff = sorted([b - a for a, b in zip(X[:-1], X[1:])], reverse=True)
    print(sum(diff[N-1:]))
    
if __name__ == '__main__':
    main()

