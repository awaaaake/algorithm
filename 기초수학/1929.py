import sys
import math
input=sys.stdin.readline
M, N=map(int, input().split())

def isprime(num): #소수냐
    if num==1:#1은 소수도, 합성수도 아니다
      return False
    for j in range(2,int(i**0.5)+1):
        if num%j==0:
            return False #나눠떨어지는게 있으면 소수가 아님
    else:
        return True

for i in range(M,N+1):
    if isprime(i):
        print(i)
