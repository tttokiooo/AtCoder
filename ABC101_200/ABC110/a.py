# https://atcoder.jp/contests/abc110/tasks/abc110_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    ABC = sorted(map(int, input().split()))
    print(ABC[2] * 10 + ABC[0] + ABC[1])

if __name__ == '__main__':
    main()
