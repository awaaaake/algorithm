import sys
input = sys.stdin.readline
N=int(input())
data=[]
for i in range(N):
    data.append(tuple(map(int, input().split())))
#map �Լ��� ��ȯ ���� map��ü �̱� ������ �ش� �ڷ����� list Ȥ�� tuple�� �� ��ȯ�����־�� �մϴ�.

sorted_data=sorted(data, key=lambda x : (x[1], x[0]))
for x, y in sorted_data:
    print(x, y)
