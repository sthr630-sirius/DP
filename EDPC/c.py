"""
dp[n] = max(dp_a[n], dp_b[n], dp_c[n])
dp_a[i] = ai + max(dp_b[i-1], dp_c[i-1])
dp_b[i] = bi + max(dp_c[i-1], dp_a[i-1])
dp_c[i] = ci + max(dp_a[i-1], dp_b[i-1])
"""
n = int(input())
a = [0]*(n+1)
b = [0]*(n+1)
c = [0]*(n+1)
dp = [0]*(n+1)
dp_a = [0]*(n+1)
dp_b = [0]*(n+1)
dp_c = [0]*(n+1)
for i in range(1, n+1):
    a[i], b[i], c[i] = map(int, input().split())

dp_a[1] = a[i]
dp_b[1] = b[i]
dp_c[1] = c[i]

for i in range(1, n+1):
    dp_a[i] = a[i] + max(dp_b[i-1], dp_c[i-1])
    dp_b[i] = b[i] + max(dp_c[i-1], dp_a[i-1])
    dp_c[i] = c[i] + max(dp_a[i-1], dp_b[i-1])
    dp[i] = max(dp_a[i], dp_b[i], dp_c[i])
"""
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(f"dp_a:{dp_a}")
print(f"db_b:{dp_b}")
print(f"dp_c:{dp_c}")
print(f"dp:{dp}")
"""
print(dp[n])