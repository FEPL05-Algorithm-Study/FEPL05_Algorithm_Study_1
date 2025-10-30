n=int(input())

f1=0
f2=f3=1
for _ in range(3,n+1):
    f1=f2+f3
    f2,f3=f3,f1

print(f1,n-2)