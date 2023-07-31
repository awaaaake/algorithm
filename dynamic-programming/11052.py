import sys
input = sys.stdin.readline

N=int(input())
P=list(map(int, input().split()))
dp=[0]*(N+1)
#dp[i]는 카드 i개를 갖기위해 지불해야하는 금액의 최댓값
for i in range(1, N+1):
    dp[i]=P[i-1]

for i in range(2,N+1):
    for j in range(1,i):
        dp[i]=max(dp[i], dp[i-j]+dp[j])
    
print(dp[N])

