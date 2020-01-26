# https://atcoder.jp/contests/abc125/tasks/abc125_c
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    A = sorted(map(int, input().split()))

    if N == 2:
        print(max(A))
        exit()

    A0, A1, A2 = A[:3]
    A_min_sq = int(math.sqrt(A2)) + 1
    
    gcd_ls = set()
    for i in range(A_min_sq, 0, -1):
        div = set()
        c = 0
        if A0 % i == 0:
            div.add(A0 // i)
            c += 1
        if A1 % i == 0:
            div.add(A1 // i)
            c += 1
        if A2 % i == 0:
            div.add(A2 // i)
            c += 1
        if c < 2:
            continue
        gcd_ls.add(i)

        for j in div:
            if A0 % j == 0 and (A1 % j == 0 or A2 % j == 0):
                gcd_ls.add(j)
            elif A1 % j == 0 and A2 % j == 0:
                gcd_ls.add(j)
    gcd_ls = sorted(gcd_ls, reverse=True)

    for i in gcd_ls:
        wa = False
        for j in A:
            if j % i != 0:
                if wa:
                    break
                wa = True
        else:
            print(i)
            exit()

if __name__ == '__main__':
    main()
