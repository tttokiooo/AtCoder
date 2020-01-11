# https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_a
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    st = [input() for i in range(n)]
    x = input()
    isStart = False
    sum = 0
    for i in st:
        s, t = i.split()
        if s == x:
            isStart = True
            continue
        if isStart:
            sum += int(t)
    print(sum)

if __name__ == '__main__':
    main()

