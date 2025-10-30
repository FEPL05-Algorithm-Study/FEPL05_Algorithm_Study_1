t=int(input())

def binet(n):
    return round((((1+(5**.5))/2)**n-((1-(5**.5))/2)**n)/(5**.5))

for _ in range(t):
    n=int(input())
    if n==0:
        print(1,0)
    elif n==1:
        print(0,1)
    else:
        print(binet(n-1),binet(n))
