# https://atcoder.jp/contests/abc149/tasks/abc149_c
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    x = int(input())
    x_sqrt = int(math.sqrt(x))

    for i in range(10000):
        for j in range(2, x_sqrt):
            if x % j == 0:
                x += 1
                break
        else:
            print(x)
            exit()

if __name__ == '__main__':
    main()
