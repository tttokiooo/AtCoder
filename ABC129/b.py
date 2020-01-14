# https://atcoder.jp/contests/abc129/tasks/abc129_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    _ = int(input())
    www = tuple(map(int, input().split()))

    min = 200
    t = - sum(www)
    for w in www:
        t += 2 * w
        if abs(t) < min:
            min = abs(t)
    print(min)

if __name__ == '__main__':
    main()
