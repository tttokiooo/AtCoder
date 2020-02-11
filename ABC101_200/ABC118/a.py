# https://atcoder.jp/contests/abc118/tasks/abc118_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)
        
if __name__ == '__main__':
    main()
