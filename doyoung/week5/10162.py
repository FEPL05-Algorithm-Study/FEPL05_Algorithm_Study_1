import sys

input = sys.stdin.readline

T = int(input()) # 입력값

time = [300, 60, 10] # 입력값이 시간초로 들어오므로 변환
result = [] # 결과값 
change = T # 나머지값을 기록하는 변수

for i in time: 
    if i > T:
        result.append(str(0))
        continue

    result.append(str(change // i))
    change %= i

# 나머지가 남아있으면 -1 아니면 정상 결과를 출력
if change != 0:
    print(-1)
else:
    print(' '.join(result))
    


    
    
    