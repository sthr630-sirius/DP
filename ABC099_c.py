"""
dp[i][j] 引出し金額の単位iまで、金額jを引出すための最小の回数
"""
n = int(input())
unit = [0, 1]

m = n
counter = 0
while m >= 6:
    m = m//6
    counter += 1
    unit.append(6**counter)

m = n
counter = 0
while m >= 9:
    m = m//9
    counter += 1
    unit.append(9**counter)

inf = 100000
dp = [[inf]*(n+1) for _ in range(len(unit))]

dp[0][0] = 0

for i in range(1, len(unit)):
    for j in range(0, n+1):
        if j-unit[i] >= 0:
            dp[i][j] = min(dp[i-1][j-unit[i]], dp[i][j-unit[i]]) + 1

        dp[i][j] = min(dp[i][j], dp[i-1][j])
#print(dp[0][:10])
#print(dp[1][:10])
#print(dp[2][:10])
#print(dp[1])
#print(dp[5])
#print(unit)
print(dp[len(unit)-1][n])

"""
ans = 0

for i in sorted(money_list, reverse=True):
    print(f"i={i}")
    ans = ans + n//i
    n = n%i
    print(f"ans={ans}")
    print(f"n={n}")
print(n)
print(ans+n)
"""