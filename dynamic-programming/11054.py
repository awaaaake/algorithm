import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp1= [1]*N #dp[i]는 해당 수를 기준으로 하는 가장 긴 바이토닉 수열의 길이
dp2= [1]*N

for i in range(1,N):
        for j in range(i):
            if A[j]<A[i]:
                dp1[i]=max(dp1[i], dp1[j]+1)
 
reversed_A=A[::-1]
for i in range(1,N):
        for j in range(i):
            if reversed_A[j]<reversed_A[i]:
                dp2[i]=max(dp2[i], dp2[j]+1)

#위의 FOR문을 반드시 다돌고 아래코드를 실행해야한다.
list = [dp1[i] + dp2[N - i - 1] - 1 for i in range(N)]
# for i in range(N): #처음에는 (1,N) 을 했다 가정 첫번째수는 바이토닉 수열이 가장 짧을 거라 생각했는데, 오히려 감소하는 뒷부분의 수열이 정말 길수도있다.
#      list.append(dp1[i]+dp2[N-i-1]-1)

print(max(list))



            

