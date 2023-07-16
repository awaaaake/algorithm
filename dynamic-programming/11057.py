import sys

N=int(sys.stdin.readline())
dp=[[0]*10 for i in range(N+1)] #2차원배열은 바깥또한 []로 감싸주기

for i in range(10):
    dp[1][i]=1

'''
i는 자릿수, j는 맨앞자리에 오는 숫자
예를들어 dp[2][3]은 십의자리에 3이오는 경우 가능한 오르막수의 개수이다.
이것은 dp[1][3]부터 dp[1][9]까지의 합이다.
'''
for i in range(2, N+1):
    for j in range(10):
        dp[i][j]=sum(dp[i-1][j:10])

print(sum(dp[N][0:10])%10007)