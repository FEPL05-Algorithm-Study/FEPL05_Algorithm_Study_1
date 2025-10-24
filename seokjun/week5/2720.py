T = int(input())
for _ in range(T):
    C = int(input())
    coins = [25,10,5,1]
    result = []
    # 큰 코인부터 먼저 계산, 계산후 남은코인을 더 작은코인으로 계산 
    for coin in coins:
        result.append(C//coin)
        C %= coin
    print(*result)