import sys
input = sys.stdin.readline

N=int(input())
dp=[0]*(31) #0���� �ʱ�ȭ�ؼ� i�� Ȧ���� ���� ���� �߰� �ڵ�x
dp[2]=3

for i in range(4,N+1):
    dp[i] = dp[i-2]*dp[2]
    if i%2 == 0:
        dp[i]+=sum(dp[2:i-3:2])*2+2 # �������� �ڽŸ��� Ư���Ѱ�� 2
        '''
        dp[i-4]���� dp[ ]*2�� ������ ������ 
        Ư���� ���� ���� ���� 4�� ������ �����ϱ� ����
        '''
print(dp[N])
    