import sys
input = sys.stdin.readline
n = int(input())
sequence=list(map(int, input().split()))
dp=sequence.copy() #dp[i]�� i��° �������� ���ӵ� ���� �ִ� ��
#copy�� �ƴ϶� copy()�޼ҵ带 ȣ���ؾ��Ѵ�.
for i in range(1,n):
    if sequence[i-1]<0:
        dp[i]=max(dp[i-1]+sequence[i],sequence[i])
    else:
        dp[i]=dp[i-1]+sequence[i]

print(max(dp))