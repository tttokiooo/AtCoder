# https://atcoder.jp/contests/abc112/tasks/abc112_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    XYH = [tuple(map(int, input().split())) for _ in range(N)]
    XYH = sorted(XYH, key=lambda x: x[2], reverse=True)

    H = -1
    for x in range(0, 101):
        for y in range(0, 101):
            for xi, yi, hi in XYH:
                abs_xy = abs(x - xi) + abs(y - yi)
                if H < 0 and hi > 0:
                    H = hi + abs_xy
                elif hi != max(H - abs_xy, 0):
                    H = -1
                    break
            else:
                if H > 0:
                    print(x, y, H)
                    exit()

if __name__ == '__main__':
    main()
