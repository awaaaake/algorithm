import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n>1:
        dp[0][1]+=dp[1][0]
        dp[1][1]+=dp[0][0]
    for i in range(2, n):#n이1인경우 이for루프는 실행되지않고 바로 print문으로 넘어간다.
        dp[0][i]+=max(dp[1][i-1], dp[1][i-2]) #지그재그로오는것과 한칸 건너뛰는 경우를 비교한다. 비교해서 더큰 경로에 자신의 dp값(점수값)을 더한다.
        dp[1][i]+=max(dp[0][i-1], dp[0][i-2]) #두경로를 모두구해야한다. 왜냐하면 끝까지 가지 않고서는 총 점수를 알수없기때문에
    print(max(dp[0][n-1], dp[1][n-1]))
