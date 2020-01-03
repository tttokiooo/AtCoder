# https://atcoder.jp/contests/abc133/tasks/abc133_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    mod = 2019
    l, r = map(int, input().split())
    l_div = l // mod
    if mod * (l_div + 2) < r:
        print(0)
        quit()
    elif mod * (l_div + 1) < r:
        print(1)
        quit()
    ans = 2020
    r_mod_1 = r % mod + 1
    for i in range(l % mod, r_mod_1):
        for j in range(i+1, r_mod_1):
            ij_mod = i * j % mod
            if ans > ij_mod:
                ans = ij_mod
    print(ans)

if __name__ == '__main__':
    main()
