# https://atcoder.jp/contests/abc112/tasks/abc112_d
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    N, M = map(int, input().split())
    m_sqrt = int(math.sqrt(M)) + 2

    ans = set()
    for i in range(1, m_sqrt):
        if M % i == 0:
            if M // i >= N:
                ans.add(i)
            if i >= N:
                ans.add(M // i)
    print(max(ans))
            
if __name__ == '__main__':
    main()
