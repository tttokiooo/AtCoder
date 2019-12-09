import sys
input = sys.stdin.readline

def main():
    n_half = int(input()) // 2
    s = input().strip('\n')
    if n_half > 0 and s[0:n_half] == s[n_half:]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
