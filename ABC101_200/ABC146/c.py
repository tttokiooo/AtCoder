# https://atcoder.jp/contests/abc146/tasks/abc146_c
a, b, x = map(int, input().split())

def search(min, max):
    v = (min + max) // 2
    c = a * v + b * len(str(v))
    if min > max:
        print(v)
    elif c == x:
        print(v)
    elif c > x:
        search(min, v - 1)
    else:
        search(v + 1, max)

search(1, 1000000000)
