def laundry(amount, coins):
    result = []
    for coin in coins:
        count = amount // coin
        result.append(count)
        amount %= coin
    return result

# 입력 받기
n = int(input())  # 입력값 개수
coins = [25, 10, 5, 1]  # 동전 종류


for _ in range(n):
    amount = int(input())  # 금액
    result = laundry(amount, coins)
    print(*result)  # 공백제거
