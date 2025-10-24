def camping(L, P, V):
    result = V // P * L # case 1,2 = 10
    if V % P < L: # case 1 V % P= 4, case 2 V % P= 1
        result += V % P
    else:
        result += L
    return result

# 입력 받기
L, P, V = map(int, input().split())
count = 1 # case 번호 1번부터 초기화

while L != 0 and P != 0 and V != 0:
    print(f"Case {count}: {camping(L, P, V)}")
    count += 1
    L, P, V = map(int, input().split())