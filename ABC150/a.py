# https://atcoder.jp/contests/abc150/tasks/abc150_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    K,X = map(int, input().split())
    if 500 * K >= X:
        print('Yes')
    else:
        print('No')
    
if __name__ == '__main__':
    main()
