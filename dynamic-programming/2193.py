import sys
N = int(sys.stdin.readline())

dp=[[0]*2 for i in range(91)] #91은 행의 개수
dp[1][1]=1 # N이 한자리일 때 1의 개수5
dp[2][0]=1


for i in range(3,N+1):
    dp[i][0]=dp[i-1][1]+dp[i-1][0]
    dp[i][1]=dp[i-1][0]

print(dp[N][0]+dp[N][1])