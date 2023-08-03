import sys
input = sys.stdin.readline

N=int(input())
data=[]

for i in range(N):
    data.append(tuple(input().split()))

sorted=sorted(data, key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in sorted:
    print(i[0])