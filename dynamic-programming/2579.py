import sys
input=sys.stdin.readline
n = int(input())
data = [0]*(n+1) #��� ������

for i in range(1,n+1):
    data[i]=int(input())

dp=[data.copy(),data.copy()] #I��° ��ġ ���������� ������ �ִ�(��찡 2����)

for i in range(2,n+1):
    dp[0][i]=max(dp[0][i-2]
                 ,dp[1][i-2])+data[i]
    dp[1][i]=dp[0][i-1]+data[i]

print(max(dp[0][n],dp[1][n]))