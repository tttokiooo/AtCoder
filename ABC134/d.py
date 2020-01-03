# https://atcoder.jp/contests/abc134/tasks/abc134_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    ls = [0] * n
    ans = []

    for i in range(n-1, -1, -1):
        if (sum(ls[i::i+1]) % 2) != a[i]:
            ls[i] = 1
            ans.append(i+1)
    print(sum(ls))
    if ans:
        print(*ans[::-1])


if __name__ == '__main__':
    main()
