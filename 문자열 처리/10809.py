import sys
S=sys.stdin.readline().strip()

list=[-1]*26
for i in range(len(S)):
    if list[ord(S[i])-97]==-1: #ó�������ϴ� ��ġ�ѹ��� �����ؾ��ϹǷ�
        list[ord(S[i])-97]=i
for i in list:
    print(i,end=' ')