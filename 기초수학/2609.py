# A, B =map(int, input().split())
# min=min(A, B)
# 최대공약수=0

# for i in range(1,min+1):
#     if A%i==0 and B%i==0 and i>최대공약수:
#         최대공약수=i
#         최소공배수=A//i*B//i*i

# print(최대공약수)
# print(최소공배수)

import math
A, B =map(int, input().split())
print(math.gcd(A,B))
print(math.lcm(A,B))