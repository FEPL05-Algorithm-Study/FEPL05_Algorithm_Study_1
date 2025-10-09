n = int(input())

answer = 0
s = 0 
i = 0

while s<n:
    # s는 0부터 i까지의 합
    s += i
    if s>=n:
        break

    # 연속된수가 i개면 a + a+1 + a+2 ... + a+i = a*(i+1) + s
    # n= a*(i+1) + s 이어야 하므로 (n-s)%(i+1)==0 이면 유효
    answer += int((n-s)%(i+1)==0)
    i += 1

print(answer)