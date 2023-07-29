import sys
input= sys.stdin.readline

n, k = map(int, input().split())

dp=[[0]*201 for i in range(201)] #for i in range(201) 행을 형성하는 부분

for i in range(201):
    dp[1][i]=1 #모든수를 1개의 정수로 나타내는 방법은 1가지이다.
    dp[2][i]=i+1 #어떤수를 2개의 정수로 나타내는 방법은 해당정수 + 1 이다.

for i in range(3, 201): #어떤 정수를 3개이상의 정수들의 합으로 나타내는 방법
    dp[i][1]=i #나머지를 0으로 채우는 경우의 수
    for j in range(2,201):
        dp[i][j]=(dp[i][j-1]+dp[i-1][j])%1000000000 #같은행의 왼쪽열, 같은열의 위쪽행
    
print(dp[k][n])