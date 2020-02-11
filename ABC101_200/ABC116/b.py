# https://atcoder.jp/contests/abc116/tasks/abc116_b
import sys
def input(): return sys.stdin.readline().rstrip()

def calc(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def main():
    s = int(input())

    val = s
    ls = set([val])
    for m in range(2, 1000001):
        val = calc(val)
        if val in ls:
            print(m)
            exit()
        else:
            ls.add(val)
    
if __name__ == '__main__':
    main()
