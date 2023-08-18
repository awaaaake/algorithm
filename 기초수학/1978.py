import sys
import math
input=sys.stdin.readline
N=int(input())
data=list(map(int, input().split()))
count=0

def isprime(num):
    if num==1: #1은 소수도, 합성수도 아니다
      return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False #나눠떨어지는게 있으면 소수가 아님
        else:
            return True

for i in data:
    if isprime(i):
        count+=1 
print(count)
'''
 for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우 else문이 실행되는 방식
'''