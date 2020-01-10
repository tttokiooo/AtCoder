# https://atcoder.jp/contests/abc150/tasks/abc150_c
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    ls = [0] * 9
    ls[0] = 1
    for i in range(N):
        ls[i+1] = ls[i] * (i+1)

    p_sum = 0
    q_sum = 0
    p_ls = [1,2,3,4,5,6,7,8]
    q_ls = [1,2,3,4,5,6,7,8]
    for j in range(N):
        p_sum += p_ls.index(P[j]) * ls[N-j-1]
        p_ls.remove(P[j])
        q_sum += q_ls.index(Q[j]) * ls[N-j-1]
        q_ls.remove(Q[j])
    
    print(abs(p_sum - q_sum))

if __name__ == '__main__':
    main()
