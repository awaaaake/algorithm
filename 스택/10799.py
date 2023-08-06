import sys
data=sys.stdin.readline().strip()

stack=[]
count=0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1]=='(':
            stack.pop() #()이면 현재 스택에있는 (수만큼 정답에 더한다.
            count+=len(stack)
        else:
            stack.pop()
            count+=1
print(count)
        
