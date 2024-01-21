n = int(input())
points = list(map(int, input().split()))
points = [0] + points
dp = [[0]*(100*n+1) for _ in range(n+1)]
dp[0][0] = 1

"""
dp[i][j]　問題iまで得点jができれば1、できなければ0
"""
for i in range(1, n+1):
    for j in range(0, 100*n+1):
        if j-points[i] >= 0 and dp[i-1][j-points[i]] == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j]

print(sum(dp[n]))
