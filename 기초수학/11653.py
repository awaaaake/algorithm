import sys
input=sys.stdin.readline
N=int(input())

while N > 1:
    for i in range(2,N+1): #int(N**0.5)+1 X -> 왜? 마지막에 N=3이라고 가정할경우 3으로 나누는 것까지 와야한다.
        if N%i==0:
            print(i)
            N=N//i
            break