N = input() # 입력값

count = 0 # 가지수

for i in range(1,int(N)+1): # 1부터 15까지
   
    num = int(N) - i * (i - 1) // 2

    if num > 0 and num % i == 0:
        a = num // i #몫 추출
        if a > 0:
            count += 1
print(count)

#  num > 0 , num % i == 0
#  i=1, num=15 15-1*0/2=15, 15%1=0, a=15 누적 count=1 (15)
#  i=2, num=14 15-2*1/2=14, 14%2=0 ,a=7 누적 count=2 (7,8)
#  i=3, num=13 15-3*2/2=12, 12%3=0 ,a=4 누적 count=3 (4,5,6)
#  i=4, num=12 15-4*3/2=9, 9%4≠0
#  i=5, num=11 15-5*4/2=5, 5%5=0 ,a=1 누적 count=4 (1,2,3,4,5)
#  i=6, num=10 15-6*5/2=0, 0%6=0 ,a=0 0은 양수가 아니기에 해당x