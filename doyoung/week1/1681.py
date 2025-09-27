value = input().split()

N = int(value[0])
L = value[1]


count = 0
last_label = 0
label = 0

while count < N:
     label += 1

     if(str(label).find(L) < 0):
        count += 1
        last_label = label
        

print(last_label)