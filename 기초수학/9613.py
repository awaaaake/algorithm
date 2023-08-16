import sys
import math
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    result=[]# 변수명과 내장 함수명이 겹치면x, result초기화는 각 테스트케이스가 반복될때마다 해주기!
    data=list(map(int, input().split()))
    for i in range(1,len(data)-1):
        for j in range(i+1, len(data)):
            result.append(math.gcd(data[i],data[j]))
    print(sum(result))