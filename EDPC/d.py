import numpy as np

n, max_w = map(int, input().split())
w = [0]*(n+1)
v = [0]*(n+1)

#dp = np.zeros((n+1, max_w+1), dtype=int)
dp = [[0]*(max_w+1) for _ in range(n+1)]

for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

#print(dp)

for i in range(1, n+1):
    for j in range(1, max_w+1):
        if j-w[i]>=0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]
    #print(dp)

print(dp[n][max_w])