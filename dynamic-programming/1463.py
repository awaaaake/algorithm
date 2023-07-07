# N = int(input())
# topdown_memo = [0]*(N+1)

# def topdown(N):
#     if N==1: #기저 상태 도달 시, 0으로 초기화
#          return 0
#     if topdown_memo[N]!=0:
#          return topdown_memo[N]  #메모에 계산된 값이 있으면 바로 반환!
#     topdown_memo[N]=topdown(N-1)+1
#     if N%2==0:
#         topdown_memo[N]=min(topdown_memo[N],topdown(N//2)+1)
#     if N%3==0:
#         topdown_memo[N]=min(topdown_memo[N],topdown(N//3)+1)
#     return topdown_memo[N]

# print(topdown(N))

N = int(input())
dp = [0]*(N+1) #dp[1]=0으로 초기화

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

print(dp[N])

# x=int(input())
# dp={1:0}
# def rec(n):
#     if n in dp.keys():
#         return dp[n]
#     if (n%3==0) and (n%2==0):
#         dp[n]=min(rec(n//3)+1, rec(n//2)+1)
#     elif n%3==0:
#         dp[n]=min(rec(n//3)+1, rec(n-1)+1)
#     elif n%2==0:
#         dp[n]=min(rec(n//2)+1, rec(n-1)+1)
#     else:
#         dp[n]=rec(n-1)+1
#     return dp[n]
# print(rec(x))