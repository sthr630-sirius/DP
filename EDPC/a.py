n = int(input())
height = list(map(int, input().split()))
dp = [0]*n
dp[1] = abs(height[1] - height[0])+dp[0]
#print(height)
#print(dp)
for i in range(2, n):
    dp[i] = min(abs(height[i]-height[i-1])+dp[i-1], abs(height[i]-height[i-2])+dp[i-2])
print(dp[n-1])