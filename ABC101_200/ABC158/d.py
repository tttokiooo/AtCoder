# https://atcoder.jp/contests/abc158/tasks/abc158_d
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    S = input()
    Q = int(input())

    reverse = False
    header = [''] * Q
    footer = [''] * Q
    for i in range(Q):
        query = input()
        if query[0] == '1':
            reverse = not reverse
        else:
            _, f, c = query.split()
            if (f == '2' if reverse else f == '1'):
                header[i] = c
            else:
                footer[i] = c

    if reverse:
        print("".join(footer[::-1] + list(S)[::-1] + header))
    else:
        print("".join(header[::-1]) + S + "".join(footer))

if __name__ == '__main__':
    main()
