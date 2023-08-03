import sys
input = sys.stdin.readline

N =int(input())
data=[]
for i in range(N):
    x, y=map(str, input().split())
    data.append((int(x),y))

sorted=sorted(data, key=lambda x: int(x[0]))
for x, y in sorted:
    print(x,y)