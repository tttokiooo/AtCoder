# https://atcoder.jp/contests/abc108/tasks/abc108_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    K = int(input())
    k2 = K // 2
    if K % 2 == 1:
        print(k2 * (k2 + 1))
    else:
        print(k2 ** 2)

if __name__ == '__main__':
    main()
