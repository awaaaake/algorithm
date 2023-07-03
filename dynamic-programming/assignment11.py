# #
# N = int(input())
# dp=[-1]*(N+1)
# dp[1]=1

# #기저상태를 저장한 후, for문돌면서 bottom-up방식
# for i in range(2, N+1):
#     if dp[i-1] != -1 and i%2==0 and dp[i//2] !=-1:
#         dp[i]=min(dp[i-1], dp[i//2]) + 1
#     elif dp[i-1] != -1:
#         dp[i]=dp[i-1]+1
#     elif  i%2==0 and dp[i//2] !=-1:
#         dp[i]=dp[i//2]+1
#     #둘다 최소값, 즉 dp값이 존재하지 않는 경우 현재값의 dp도 구할수없기에 -1그대로 둔다.
# print(dp[N])


# '''
# n=1부터 차례대로 f(n)을 계산해보면 
# f(n)=f(n-1)+f(n-2)+f(n-3)이라는 점화식이 구해진다.
# '''
# n_list=[]
# topdown_memo=[0]*31#31일까지해야 30번째인덱스가생김
# #기저 상태 도달 시, 1,2,4로 초기화
# topdown_memo[1]=1
# topdown_memo[2]=2
# topdown_memo[3]=4

# for i in range(4,31):
#     topdown_memo[i]= sum(topdown_memo[i-3:i])#topdown_memo[i-1]+topdown_memo[i-2]+topdown_memo[i-3]

# k=int(input())
# print(topdown_memo[k])


N = int(input())
dp=[-1]*(N+1)
prices=list(map(int, input().split()))

#초기화
for i in range(1, N+1):
    dp[i]=prices[i-1]
#기저상태를 저장한 후, for문돌면서 bottom-up방식
for i in range(2, N+1):
    for k in range(1, i):
        if (dp[i-k]+prices[k-1])>dp[i]:
            dp[i]=dp[i-k]+dp[k]
print(dp[N])