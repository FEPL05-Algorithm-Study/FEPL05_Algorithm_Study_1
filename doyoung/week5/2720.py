import sys

input = sys.stdin.readline

T = int(input())

cent = [25, 10, 5, 1] # 입력값이 센트이므로 동일하게 변경 

for i in range(T):
    change = []
    c = int(input()) # 입력값

    for j in cent:
        change.append(str(c // j)) # 동전개수 추가
        c %= j # 거슬러주고 남은 금액 입력

    print(' '.join(change)) # join으로 출력

    
    
    

    
    
