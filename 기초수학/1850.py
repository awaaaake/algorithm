import sys
input=sys.stdin.readline
A, B=map(int,input().split()) #A>B
if A < B:
    A,B=B,A
def gcd(a,b):
    while b>0:
        a, b=b, a%b
    return a

print('1'*gcd(A, B)) #1�� ������ �ƴ� ���ڿ����ؾ��� a������ŭ 1�� ������ ��µȴ�.
