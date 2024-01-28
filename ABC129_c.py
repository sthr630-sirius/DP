"""
dp[i] 位置iまでの移動の通り数
位置Aiの移動は0通り
"""
n, m = map(int, input().split())

ng_step = [False]*(n+1)
for _ in range(m):
    ng_step[int(input())] = True

dp = [0]*(n+1)

dp[0] = 1
if ng_step[1]:
    dp[1] = 0
else:
    dp[1] = 1

for i in range(2, n+1):
    if ng_step[i]:
        dp[i] = 0
    else:
        dp[i] = (dp[i-1] + dp[i-2])%1000000007

print(dp[n])