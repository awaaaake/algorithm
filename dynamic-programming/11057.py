import sys

N=int(sys.stdin.readline())
dp=[[0]*10 for i in range(N+1)] #2�����迭�� �ٱ����� []�� �����ֱ�

for i in range(10):
    dp[1][i]=1

'''
i�� �ڸ���, j�� �Ǿ��ڸ��� ���� ����
������� dp[2][3]�� �����ڸ��� 3�̿��� ��� ������ ���������� �����̴�.
�̰��� dp[1][3]���� dp[1][9]������ ���̴�.
'''
for i in range(2, N+1):
    for j in range(10):
        dp[i][j]=sum(dp[i-1][j:10])

print(sum(dp[N][0:10])%10007)