# https://atcoder.jp/contests/abc115/tasks/abc115_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    D = int(input())
    print('Christmas' + ' Eve' * (25 - D))
    
if __name__ == '__main__':
    main()

