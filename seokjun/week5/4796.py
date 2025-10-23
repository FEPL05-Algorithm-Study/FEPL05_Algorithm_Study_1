i = 1
while True:
    L,P,V = map(int,input().split())
    if L==P==V==0:
        break
    maxday = (V//P)*L + min((V%P),L)
    print(f'Case {i}: {maxday}')
    i += 1