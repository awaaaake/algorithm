import sys
input = sys.stdin.readline
n = int(input())
sequence=list(map(int, input().split()))
dp=sequence.copy() #dp[i]는 i번째 수까지의 연속된 수의 최대 합
#copy가 아니라 copy()메소드를 호출해야한다.
for i in range(1,n):
    if sequence[i-1]<0:
        dp[i]=max(dp[i-1]+sequence[i],sequence[i])
    else:
        dp[i]=dp[i-1]+sequence[i]

print(max(dp))