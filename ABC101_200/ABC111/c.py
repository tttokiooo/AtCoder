# https://atcoder.jp/contests/abc111/tasks/abc111_c
import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    v = tuple(map(int, input().split()))

    c_odd_most =  Counter(v[1::2]).most_common(2)
    c_even_most =  Counter(v[::2]).most_common(2)

    c_odd = c_odd_most[0][1]
    c_odd2 = c_odd_most[1][1] if len(c_odd_most) > 1 else 0
    c_even = c_even_most[0][1]
    c_even2 = c_even_most[1][1] if len(c_even_most) > 1 else 0

    if c_odd_most[0][0] == c_even_most[0][0]:
        if c_odd + c_even2 > c_odd2 + c_even:
            c_even = c_even2
        else:
            c_odd = c_odd2
    
    print(n - c_odd - c_even)

if __name__ == '__main__':
    main()
