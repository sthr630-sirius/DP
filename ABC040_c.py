"""
dp[i] 位置iにいくまでに必要なコストの最小値
dp[i] = min(dp[i-1]+|tree[i]-tree[i-1]|, dp[i-2]+|tree[i]-tree[i-2]|)
"""
n = int(input())
tree = [0] + list(map(int, input().split()))

inf = 10**9+1
dp = [inf]*(n+1)

dp[1] = 0
dp[2] = dp[1]+abs(tree[2]-tree[1])
for i in range(3, n+1):
    dp[i] = min(dp[i-1]+abs(tree[i]-tree[i-1]), dp[i-2]+abs(tree[i]-tree[i-2]))
print(dp[n])
