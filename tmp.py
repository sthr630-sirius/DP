w = int(input())
n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
print(ab)

dp = [[[0]*(w+1) for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    print(dp[i])