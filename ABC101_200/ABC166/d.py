# https://atcoder.jp/contests/abc166/tasks/abc166_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    X = int(input())
    for a in range(-120, 120):
        a5 = a ** 5
        for b in range(-120, 120):
            if a5 - b ** 5 == X:
                print(a, b)
                exit()

if __name__ == '__main__':
    main()
