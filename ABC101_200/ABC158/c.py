# https://atcoder.jp/contests/abc158/tasks/abc158_c
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    A, B = map(int, input().split())
    a = math.floor(A // 0.08)

    for i in range(a, a + 20):
        if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()
