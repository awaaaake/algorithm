import sys
input = sys.stdin.readline

n = int(input())
data = [0]*10000
for i in range(n):
    data[i] = int(input())

#dp[i]는 i번째 포도주까지 최대로 마신 포도주의 양
dp = [0]*10000
dp[0] = data[0]
dp[1] = data[0]+data[1]
dp[2] = max(data[1]+data[2], dp[1], data[2]+dp[0])
#자신을 포함하는 경우와 포함하지 않는 경우를 모두 고려
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+data[i-1]+data[i], dp[i-2]+data[i])

print(dp[n-1])
