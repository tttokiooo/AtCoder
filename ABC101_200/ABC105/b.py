# https://atcoder.jp/contests/abc105/tasks/abc105_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())

    for i in range(26):
        for j in range(15):
            if N == 4 * i + 7 * j:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()
