# https://atcoder.jp/contests/abc152/tasks/abc152_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    
    res = [[0] * 10 for _ in range(10)]
    for i in range(1, n+1):
        s = str(i)
        if s[-1] == '0':
            continue
        res[int(s[0])][int(s[-1])] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += res[i][j] * res[j][i]
    print(ans)

if __name__ == '__main__':
    main()
