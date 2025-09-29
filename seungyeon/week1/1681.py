N,L = list(map(int,input().split(' ')))
L = str(L)

plus = 0
i = 1
while True:
    if str(L) not in str(i):
        plus += 1
        if(plus == N):
            print(i)
            break
    i += 1