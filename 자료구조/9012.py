T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:# 스택에 괄호가 없을경우 NO -> 짝이 맞지 않는 경우
                print("NO")
                break
        else:# break문으로 끊기지 않고 수행됬을경우 수행한다
            if not stack:# break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
                print("YES")
            else:# break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
                print("NO")
# T = int(input())
# data = []
# for i in range(T):
#     data.append(input())

# def vps(text):
#     text = text.replace("()","vps")

    
#     while(True):
#         text = text.replace("(vps)","vps")
    
#         while "vpsvps" in text: #not in이 아님. 포함되어있는 동안에 계속 변경하는 것
#             text = text.replace("vpsvps","vps")

#         if "(vps)" not in text:
#             break

#     if "(" in text or ")" in text:
#         '''
#         if "(" or ")" in text:는 항상 참으로 평가되므로, 
#         ("(" in text)와 (")" in text)를 개별적으로 검사하기 위해선
#         따로 따로 써줘야함
#         '''
#         print("NO")
#     else:
#         print("YES")

# for text in data:
#     vps(text)
