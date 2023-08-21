import sys

input=sys.stdin.readline
N=int(input())
result=1

while N > 1:
    result*=N
    N-=1

result=str(result)
i=len(result)-1
count=0

while result[i]=='0' and i>=0: #0이아닌 숫자가 나올 때까지
    count+=1
    i-=1
print(count)

