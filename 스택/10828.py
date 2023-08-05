import sys
input= sys.stdin.readline

stack=[]
N=int(input())
for _ in range(N):
    cmd=input().split()
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop()) #그냥 stack.pop()만쓰면 pop된 원소가 출력되지 않음
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        if len(stack)==0:
            print(1)
        else: 
            print(0)
    elif cmd[0]=='top':
        if len(stack)==0:
            print(-1)
        else: 
            print(stack[-1]) #or stack[len(stack)-1]
