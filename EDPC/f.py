"""
dp[i][j] sのiまでとtのjまでを使った部分文字列の最大長
"""
def dp_print(m, x):
    for i in range(x):
        print(m[i])

s = list(input())
t = list(input())
s_len = len(s)
t_len = len(t)
s = ["0"] + s
t = ["0"] + t
dp = [[0]*(t_len+1) for _ in range(s_len+1)]
ans = ""
for i in range(1, s_len+1):
    for j in range(1, t_len+1):
        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #dp_print(dp, s_len+1)
    #print("------------")

i = s_len
j = t_len

while i > 0 and j > 0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        ans = s[i] + ans
        i -= 1
        j -= 1

print(ans)