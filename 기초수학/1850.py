import sys
input=sys.stdin.readline
A, B=map(int,input().split()) #A>B
if A < B:
    A,B=B,A
def gcd(a,b):
    while b>0:
        a, b=b, a%b
    return a

print('1'*gcd(A, B)) #1을 정수가 아닌 문자열로해야지 a개수만큼 1이 더해져 출력된다.
