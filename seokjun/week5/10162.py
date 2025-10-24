T = int(input())
# 최소 단위가 10이므로 10으로 나누어떨어지지않으면 불가능
if T%10 == 0:
    T /= 10
    buttons = [30,6,1]
    result = []
    # 시간이 큰 버튼부터 누름
    for b in buttons:
        result.append(int(T//b))
        T %= b 
    print(*result)
else:
    print(-1)