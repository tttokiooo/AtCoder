# https://atcoder.jp/contests/abc106/tasks/abc106_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    K = int(input())
    if len(S) > K and S[K-1] == '1':
        print('1')
        exit()
    for i in list(S):
        if i != '1':
            print(i)
            exit()
    print('1')

if __name__ == '__main__':
    main()
