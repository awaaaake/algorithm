import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp1= [1]*N #dp[i]�� �ش� ���� �������� �ϴ� ���� �� ������� ������ ����
dp2= [1]*N

for i in range(1,N):
        for j in range(i):
            if A[j]<A[i]:
                dp1[i]=max(dp1[i], dp1[j]+1)
 
reversed_A=A[::-1]
for i in range(1,N):
        for j in range(i):
            if reversed_A[j]<reversed_A[i]:
                dp2[i]=max(dp2[i], dp2[j]+1)

#���� FOR���� �ݵ�� �ٵ��� �Ʒ��ڵ带 �����ؾ��Ѵ�.
list = [dp1[i] + dp2[N - i - 1] - 1 for i in range(N)]

# for i in range(N): #ó������ (1,N) �� �ߴ� ���� ù��°���� ������� ������ ���� ª�� �Ŷ� �����ߴµ�, ������ �����ϴ� �޺κ��� ������ ���� ������ִ�.
#      list.append(dp1[i]+dp2[N-i-1]-1)

print(max(list))



            

