# import sys
# input = sys.stdin.readline

# N=int(input())
# data=[]
# for i in range(N):
#     data.append(int(input()))

# for i in range(N-1):
#     min = i
#     for j in range(i+1,N):
#         if data[min] > data[j]:
#             min=j
#     data[min], data[i] = data[i], data[min]

# for i in data:
#     print(i)

import sys
input = sys.stdin.readline

N=int(input())
data=[]
for i in range(N):
    data.append(int(input()))

data.sort()
for i in data:
    print(i)
