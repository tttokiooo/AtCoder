# https://atcoder.jp/contests/abc166/tasks/abc166_e
import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = map(int, input().split())
    Aplus = [0] * N
    for i, a in enumerate(A):
        Aplus[i] = i + a + 1
    A_counter = Counter(Aplus)

    ans = 0
    for i in range(1, N + 1):
        key = i * 2 - Aplus[i-1]
        ans += A_counter[key]
        if key == Aplus[i - 1]:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
