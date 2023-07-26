import sys
input = sys.stdin.readline
N=int(input())
dp = [x for x in range (N+1)]

for i in range(1,N+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i]>dp[i-j*j]+1:
            dp[i]=dp[i-j*j]+1
print(dp[N])
            
# for i in range(1, N+1):
#     sqrt_i = int(math.sqrt(i))
#     if i==(sqrt_i**2):
#         dp[i]=1
#     else:
#         dp[i]=dp[i-sqrt_i**2]+1
#         if i==100000:
#             print(i-sqrt_i**2)

# print(dp[N])