import sys
input=sys.stdin.readline
N, M=map(int, input().split())
def count_k(n,k): #n!에서 k의 개수 구하기
    cnt=0
    while n>0:
        n=n//k
        cnt+=n
    return cnt
five_count=count_k(N,5)-count_k(M,5)-count_k(N-M,5) #5의 개수
two_count=count_k(N,2)-count_k(M,2)-count_k(N-M,2) #2의 개수를 미리 구한다.
#두개중에 최소값이 0의 개수이다
print(min(five_count,two_count))