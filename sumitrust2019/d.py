# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
n,s = [input() for i in range(2)]
c = 0
for i in range(1000):
    if i < 10:
        a1 = '0'
        a2 = '0'
        a3 = str(i)
    elif i < 100:
        a1 = '0'
        a2 = str(i)[0]
        a3 = str(i)[1]
    else:
        a1 = str(i)[0]
        a2 = str(i)[1]
        a3 = str(i)[2]
    p1 = s.find(a1)
    if p1 >= 0:
        p2 = s.find(a2, p1 + 1)
        if p2 >= 0:
            if s.find(a3, p2 + 1) >= 0:
                c += 1
print(c)
