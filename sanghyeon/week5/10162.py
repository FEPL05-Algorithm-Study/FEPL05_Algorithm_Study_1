def timer(amount, T):
    result = []
    for time in T:
        count = amount // time
        result.append(count)
        amount %= time
    return result

# 입력 받기
T = [300, 60, 10]  # 버튼 5분, 1분, 10초


amount = int(input())  # 총 시간
result = timer(amount, T)
if amount % 10 != 0:
    print(-1)
else:
    print(*result)  
