N = int(input())
A = list(map(int, input().split()))
dp = A.copy()  # dp[i]: i번째 수까지 부분수열의 최대합
'''
dp에 그냥 A를 바로 대입하거나, dp = [A for i in range(2)] 이런식으로 작성하면,
dp 리스트의 각 요소들은 같은 객체를 참조하게 된다. 
따라서 dp 리스트 내부의 요소들을 수정하면 A 리스트도 영향을 받게 된다.
'''
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp)) #굳이 max(dp[0:N])이라 하지X