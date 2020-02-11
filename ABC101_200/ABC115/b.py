# https://atcoder.jp/contests/abc115/tasks/abc115_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]
    print(sum(P) - max(P) // 2)
    
if __name__ == '__main__':
    main()

