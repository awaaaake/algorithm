import sys
data = sys.stdin.readline().strip()

n = len(data)
dp = [0]*(5001)
if data[0] == '0':
    print(0)
else:
    dp[0]=dp[1]=1
    for i in range(2, n+1):
        if int(data[i-1])>0:
            dp[i]=dp[i-1]
        if 10 <= int(data[i-2:i]) and int(data[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    print(dp[n] % 1000000)