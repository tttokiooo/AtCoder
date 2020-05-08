# https://atcoder.jp/contests/abc109/tasks/abc109_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())

    pre = input()
    said = set([pre])
    for _ in range(N - 1):
        W = input()
        if W in said or pre[-1] != W[0]:
            print('No')
            exit()
        pre = W
        said.add(W)
    print('Yes')

if __name__ == '__main__':
    main()
