N, L = map(int, input().split())
# N은 찾고자 하는 숫자
# L은 제외할 숫자

label = 0 # 최종 값
count = 0 # 유효한 숫자
number = 1 # 1부터 검사 시작

while True:
    if str(L) not in str(number):  
        # not in 포함하지 않음을 의미 따라서 L이 포함되지 않은 숫자를 찾음
        label = number # 해당 숫자를 최종 값으로 저장
        count += 1 # count = count + 1

    if count == N: # 유효한 숫자가 N이 되면 종료
        break

    number += 1 # number = number + 1

print(label) # 22 출력

# number =1 , 유효하지 않음 , count = 0
# number =2 , count = 1
# number =3 , count = 2
# number =4 , count = 3
# number =5 , count = 4
# number =6 , count = 5
# number =7 , count = 6
# number =8 , count = 7
# number =9 , count = 8
# number =10 , 유효하지 않음, count = 8
# number =11 , 유효하지 않음, count = 8
# number =12 , 유효하지 않음, count = 8
# number =13 , 유효하지 않음, count = 8
# number =14 , 유효하지 않음, count = 8
# number =15 , 유효하지 않음, count = 8
# number =16 , 유효하지 않음, count = 8
# number =17 , 유효하지 않음, count = 8
# number =18 , 유효하지 않음, count = 8
# number =19 , 유효하지 않음, count = 8
# number =20 , count = 9
# number =21 , 유효하지 않음, count = 9
# number =22 , count = 10 
