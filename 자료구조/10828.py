import sys
n = int(sys.stdin.readline())
stack=[]

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())# pop하면서 출력, 그냥 stack.pop() 은 출력이 안됨
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

# N = int(input())
# stack = []
# cmd = []
# for i in range(N):
#     cmd.append(input().split())

# for text in cmd:
#     # 공백은 없는 문자로 취급하고 아예 리스트에 담기지 않음
#     # text[1]로 접근하면 오류가 발생할 수 있음
#     if text[0] == "push":
#         num = int(text[1])
#         stack.append(num)
#     else:
#         text = text[0]
#         if text == "pop":
#             if len(stack) == 0:
#                 print(-1)
#             else:
#                 print(stack.pop())  # pop하면서 출력, 그냥 stack.pop() 은 출력이 안됨
#         elif text == "size":
#             print(len(stack))
#         elif text == "empty":
#             if len(stack) == 0:
#                 print(1)
#             else:
#                 print(0)
#         elif text == "top":
#             if len(stack) == 0:
#                 print(-1)
#             else:
#                 print(stack[-1])
#         else:
#             print("알수없는 명령어")
