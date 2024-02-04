"""
dp[i][j] 数字iまでを使った数式で答えがjとなる数式の数
"""
n = int(input())
num_list = list(map(int, input().split()))
ans = num_list.pop()
num_list = [0] + num_list

dp = [[0]*21 for _ in range(n+1)]
dp[1][num_list[1]] = 1

for i in range(1, n-1):
    for j in range(21):
        if dp[i][j] != 0:
            if j-num_list[i+1] >= 0:
                dp[i+1][j-num_list[i+1]] += dp[i][j]
            if j+num_list[i+1] <= 20:
                dp[i+1][j+num_list[i+1]] += dp[i][j]

print(dp[n-1][ans])