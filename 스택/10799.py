import sys
data=sys.stdin.readline().strip()

stack=[]
count=0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1]=='(':
            stack.pop() #()�̸� ���� ���ÿ��ִ� (����ŭ ���信 ���Ѵ�.
            count+=len(stack)
        else:
            stack.pop()
            count+=1
print(count)
        
