# https://atcoder.jp/contests/abc114/tasks/abc114_b
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    ans = 1000
    for i in range(len(S) - 2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

if __name__ == '__main__':
    main()
