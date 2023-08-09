import sys
input= sys.stdin.readline

data=input().rstrip('\n')
list=[]
for i in range(len(data)):
    list.append(data[i:])
list.sort()
for i in list:
    print(i)
