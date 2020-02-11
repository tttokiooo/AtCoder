# https://atcoder.jp/contests/abc141/tasks/abc141_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, k, q = map(int, input().split())
    qk = q - k
    l = [0] * (n+1)
    for _ in range(q):
        l[int(input())] += 1
    print('\n'.join(['Yes' if (i > qk) else 'No' for i in l][1:]))

if __name__ == '__main__':
    main()
