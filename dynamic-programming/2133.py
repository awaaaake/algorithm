import sys
input = sys.stdin.readline

N=int(input())
dp=[0]*(31) #0으로 초기화해서 i가 홀수인 경우는 따로 추가 코드x
dp[2]=3

for i in range(4,N+1):
    dp[i] = dp[i-2]*dp[2]
    if i%2 == 0:
        dp[i]+=sum(dp[2:i-3:2])*2+2 # 마지막에 자신만의 특수한경우 2
        '''
        dp[i-4]까지 dp[ ]*2를 더해준 이유는 
        특수한 경우는 가로 길이 4일 때부터 시작하기 때문
        '''
print(dp[N])
    