# https://atcoder.jp/contests/abc136/tasks/abc136_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ans = 0
    for i in range(5):
        isAdd = i % 2 == 0
        if n < 10 ** (i+1):
            if isAdd:
                ans += n - 10 ** i + 1
            break
        elif isAdd:
            ans += 10 ** (i+1) - 10 ** i
    print(ans)

if __name__ == '__main__':
    main()
