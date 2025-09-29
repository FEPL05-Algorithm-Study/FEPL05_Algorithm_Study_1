n, l = map(int,input().split(' '))

i = 0
answer = 0

while i<n:
    answer += 1

    # 숫자에 l이 포함되면 건너뛰기
    if not str(l) in str(answer):
        i += 1
    

print(answer)