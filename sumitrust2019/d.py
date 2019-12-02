# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
n,s = [input() for i in range(2)]
c = 0
for i in range(1000):
    v = str(i).zfill(3)
    p1 = s.find(v[0])
    if p1 >= 0:
        p2 = s.find(v[1], p1 + 1)
        if p2 >= 0:
            if s.find(v[2], p2 + 1) >= 0:
                c += 1
print(c)
