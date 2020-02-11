# https://atcoder.jp/contests/abc139/tasks/abc139_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
        return None

    total = 1
    for i in range(1, 20):
        total += a - 1
        if total >= b:
            print(i)
            return None

if __name__ == '__main__':
    main()
