import sys
input = sys.stdin.readline
dp=[1]*101 #P[N]
dp[4], dp[5]=2,2

T=int(input())

for i in range(6,101):
        dp[i]=dp[i-1]+dp[i-5]

for i in range(T):
    N=int(input())
    print(dp[N])