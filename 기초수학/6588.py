import sys
import math
input = sys.stdin.readline

array = [True for i in range(1000001)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(1000000)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= 1000000:
            array[i * j] = False
            j += 1

while True:
    n=int(input())
    if n==0:
        break

    k=n//2
    sub=0
    max=(0,0)
    for i in range(3, k+1):
        if array[i] and array[n-i]:
            if abs(n-2*i) > sub: 
                sub=abs(n-2*i)
                max=(i, n-i)
            else:
                break
    if(max==(0,0)):
        print("Goldbach's conjecture is wrong.")
    else:
        a, b = max
        print(f"{n} = {a} + {b}")



