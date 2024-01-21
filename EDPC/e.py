"""
dp[i][j] 品物iまで、価値jとしたときの重さの最小値
"""
n, w = map(int, input().split())
weight = [0]*(n+1)
value = [0]*(n+1)
v_max = n*1000

for i in range(1,n+1):
    weight[i], value[i] = map(int, input().split())

inf = 1000000001

dp = [[inf]*(v_max+1) for _ in range(n+1)]

dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, v_max+1):
        if j-value[i]>=0 and dp[i-1][j-value[i]] != inf:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-value[i]] + weight[i])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j])

for j in range(1, v_max+1):
    if dp[n][j] <= w:
        ans = j
print(ans)