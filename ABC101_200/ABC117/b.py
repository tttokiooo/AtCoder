# https://atcoder.jp/contests/abc117/tasks/abc117_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _ = int(input())
    L = tuple(map(int, input().split()))

    sum_l = sum(L)
    for l in L:
        if 2 * l >= sum_l:
            print('No')
            break
    else:
        print('Yes')
    
if __name__ == '__main__':
    main()
