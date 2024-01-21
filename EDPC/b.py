"""
TLE python code
cpp code passed test case
"""

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [1000000000]*n
dp[0] = 0
for i in range(1, n):
    for j in range(1, k+1):
        if i-j>=0:
            dp[i] = min(dp[i], abs(h[i]-h[i-j]) + dp[i-j])
        if i-j < 0:
            break
#print(h)
print(dp[n-1])

"""
#include<iostream>
#include<vector>
using namespace std;
int main(){
    long long n, k;
    long long inf;
    cin >> n >> k;
    inf = 1000000000;
    vector<long long> h(n);
    vector<long long> dp(n, inf);
    for (long long i=0; i<n; i++) cin >> h[i];

    //cout << dp[n-1] << endl;

    dp[0] = 0;

    for (long long i=1; i<n; i++){
        for (long long j=1; j<k+1; j++){
            if (i-j>=0){
                dp[i] = min(dp[i], abs(h[i]-h[i-j])+dp[i-j]);
            }
        }
    }

    cout << dp[n-1] << endl;
    return 0;
}
"""