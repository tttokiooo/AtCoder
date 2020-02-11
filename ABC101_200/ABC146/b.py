# https://atcoder.jp/contests/abc146/tasks/abc146_b
n = int(input())
s = input()
len = len(s)

ans = ''
for i in range(len):
    num = ord(s[i]) + n
    if num > 90:
        num -= 26
    ans += chr(num)
print(ans)
