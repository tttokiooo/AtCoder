# https://atcoder.jp/contests/abc116/tasks/abc116_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        h = H[i]
        if h == 0:
            continue
        for j in range(h):
            for k in range(i, N):
                if H[k] >= 1:
                    H[k] -= 1
                else:
                    break
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
