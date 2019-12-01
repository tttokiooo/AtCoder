# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
import math

n = int(input())
x = math.ceil(n / 108 * 100)

if math.floor(x * 108 / 100) == n:
    print(x)
else:
    print(':(')
