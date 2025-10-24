n = int(input())
dp = [10**16]*(n+1)
dp[0] = 0
coins = [2,5]
for i in range(n+1):
    for c in coins:
        if i-c>=0:
            # 현재금액을 거슬러줄때 코인의 최소개수  = 
            # min(현재금액을 거슬러줄때 코인의 최소개수, 
            # (현재금액-코인)금액을 거슬러줄때 코인의 최소개수 +1)
            dp[i] = min(dp[i],dp[i-c]+1)

print(-1 if dp[n]==10**16 else dp[n])
