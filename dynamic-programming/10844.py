import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]* 101 for i in range(n+1)]
for i in range(10):
    dp[1][i]=1

for i in range(2, n+1):
    for j in range(10):
        if j==0:
            dp[i][j]=dp[i-1][1] #예를들어 dp[3][1]을 구하려면 dp[2][0]이 필요함
        elif j==9:
            dp[i][j]=dp[i-1][8]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n][1:10])%1000000000)