# https://atcoder.jp/contests/abc116/tasks/abc116_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    AB, BC, CA = map(int, input().split())
    print(AB * BC // 2)
    
if __name__ == '__main__':
    main()
