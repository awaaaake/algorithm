import sys
input = sys.stdin.readline

N = int(input())
dp = [1]*N  # i번째 수까지 최대 부분수열의 길이
A = list(map(int, input().split()))

for i in range(1, N):
	for j in range(i): #그 직전 값까지
		if A[i] < A[j]:
			dp[i]=max(dp[i], dp[j]+1)
print(max(dp))