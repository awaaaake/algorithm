import sys
input= sys.stdin.readline

n, k = map(int, input().split())

dp=[[0]*201 for i in range(201)] #for i in range(201) ���� �����ϴ� �κ�

for i in range(201):
    dp[1][i]=1 #������ 1���� ������ ��Ÿ���� ����� 1�����̴�.
    dp[2][i]=i+1 #����� 2���� ������ ��Ÿ���� ����� �ش����� + 1 �̴�.

for i in range(3, 201): #� ������ 3���̻��� �������� ������ ��Ÿ���� ���
    dp[i][1]=i #�������� 0���� ä��� ����� ��
    for j in range(2,201):
        dp[i][j]=(dp[i][j-1]+dp[i-1][j])%1000000000 #�������� ���ʿ�, �������� ������
    
print(dp[k][n])