import sys
import math
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    result=[]# ������� ���� �Լ����� ��ġ��x, result�ʱ�ȭ�� �� �׽�Ʈ���̽��� �ݺ��ɶ����� ���ֱ�!
    data=list(map(int, input().split()))
    for i in range(1,len(data)-1):
        for j in range(i+1, len(data)):
            result.append(math.gcd(data[i],data[j]))
    print(sum(result))