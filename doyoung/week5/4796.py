import sys

input = [list(map(int, line.split())) for line in sys.stdin.readlines()] # 입력값 한줄로 받기

for i, date in enumerate(input, 1) :
    L, P, V = date[0], date[1], date[2] # 각각의 일수 변수저장

    if L == V == P == 0: # 0 0 0 일때 종료
        break

    # 각 조건에 맞게 출력
    if V % P <= L:
        result = V // P * L + V % P 
    elif V % P > L:  
        result = V // P * L + L
    
    print(f"Case {i}: {result}" )



    