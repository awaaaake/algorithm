import sys
import math
input=sys.stdin.readline
N=int(input())
result=1

while N > 1:
    result*=N
    N-=1
print(result)

def factorial(n):
    if(n>1):
        return n*factorial(n-1) #n*n-1*n-2*....*1
    else:
        return 1
    
print(factorial(N))

print(math.factorial(N))
