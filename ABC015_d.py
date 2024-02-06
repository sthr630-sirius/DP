import copy
"""
dp[i][k][j] スクリーンiまでを使って、枚数k枚以下、幅j以下で価値vの最大値
"""
W = int(input())
N, K = map(int, input().split())
width = [0]*(N+1)
value = [0]*(N+1)
for i in range(1, N+1):
    width[i], value[i] = map(int, input().split())

#print(width)
#print(value)

dp_prev = [[0]*(W+1) for _ in range(K+1)]
dp_next = [[0]*(W+1) for _ in range(K+1)]


for i in range(1, N+1):
    for k in range(1, K+1):
        for j in range(W+1):
            if j-width[i] >= 0:
                dp_next[k][j] = dp_prev[k-1][j-width[i]] + value[i]

            dp_next[k][j] = max(dp_next[k][j], dp_prev[k][j])

    dp_prev, dp_next = dp_next, dp_prev
    #print(dp[0])
    #print(dp[1])
    #print(dp[2])

#for i in range(N+1):
#    print(dp[i])

print(dp_prev[K][W])