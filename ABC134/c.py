# https://atcoder.jp/contests/abc134/tasks/abc134_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = tuple(map(int, [input() for _ in range(n)]))
    max_a, max_a2 = sorted(a, reverse=True)[:2]
    print('\n'.join(map(str, [max_a if i != max_a else max_a2 for i in a])))

if __name__ == '__main__':
    main()
