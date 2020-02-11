# https://atcoder.jp/contests/abc123/tasks/abc123_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    AtoE = [int(input()) for _ in range(5)]
    k = int(input())

    for i in AtoE:
        for j in AtoE:
            if abs(i - j) > k:
                print(':(')
                exit()
    else:
        print('Yay!')

if __name__ == '__main__':
    main()
