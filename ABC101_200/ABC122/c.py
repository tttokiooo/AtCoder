# https://atcoder.jp/contests/abc122/tasks/abc122_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n, q = map(int, input().split())
    s = input()

    ans = [0] * (n + 1)
    pre = ''
    sum = 0
    for i, w in enumerate(s):
        if pre == 'A' and w == 'C':
            sum += 1
        ans[i+1] = sum
        pre = w
    
    for i in range(q):
        l, r = map(int, input().split())
        print(ans[r] - ans[l])

if __name__ == '__main__':
    main()
