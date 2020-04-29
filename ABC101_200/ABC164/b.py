# https://atcoder.jp/contests/abc164/tasks/abc164_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B, C, D = map(int, input().split())
    A_dead = (A + D - 1) // D
    C_dead = (C + B - 1) // B
    if A_dead >= C_dead:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
