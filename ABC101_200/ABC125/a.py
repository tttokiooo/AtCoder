# https://atcoder.jp/contests/abc125/tasks/abc125_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, T = map(int, input().split())
    print(int((T + 0.5) // A * B))

if __name__ == '__main__':
    main()
