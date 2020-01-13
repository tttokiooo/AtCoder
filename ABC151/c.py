# https://atcoder.jp/contests/abc151/tasks/abc151_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    ac = set()
    wa = [0] * (n+1)

    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if p in ac:
            continue
        if s == 'AC':
            ac.add(p)
        elif s == 'WA':
            wa[p] += 1
    wa = [j for i, j in enumerate(wa) if i in ac]
    print(len(ac), sum(wa))

if __name__ == '__main__':
    main()
