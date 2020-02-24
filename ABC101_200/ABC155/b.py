# https://atcoder.jp/contests/abc155/tasks/abc155_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    A = tuple(map(int, input().split()))

    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

if __name__ == '__main__':
    main()
