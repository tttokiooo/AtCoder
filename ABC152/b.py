# https://atcoder.jp/contests/abc152/tasks/abc152_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())

    if a > b:
        print(str(b) * a)
    else:
        print(str(a) * b)
  
if __name__ == '__main__':
    main()
