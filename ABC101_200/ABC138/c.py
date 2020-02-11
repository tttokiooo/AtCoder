# https://atcoder.jp/contests/abc138/tasks/abc138_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    v = sorted(tuple(map(int, input().split())))
    val = v[0]
    for i in v[1:]:
        val = (val + i) / 2
    print(val)

if __name__ == '__main__':
    main()
