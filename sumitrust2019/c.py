# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
x = int(input())
v = x // 100
modv = x % 100

if v > 0 and modv / v <= 5:
    print(1)
else:
    print(0)
