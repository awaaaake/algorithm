import sys
input = sys.stdin.readline
n, k = map(int, input().split())
stack=[i for i in range(1,n+1)]
list=[]

turn=k-1

for _ in range(n): #while True:�� ����
    list.append(stack.pop(turn))
    if not stack:
        break
    turn=(turn+k-1)%len(stack) #turn���ִ� ��Ұ� pop�����Ƿ�, �ε����� ��ĭ���и�->-1���ְ�, ������ ũ�Ⱑ ��ӹٲ�Ƿ�, ����ũ��� ���� ������

print('<'+', '.join(str(i) for i in list)+'>')
