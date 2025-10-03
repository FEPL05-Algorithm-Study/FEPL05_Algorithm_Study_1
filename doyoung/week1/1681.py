value = input().split()

N = int(value[0])
L = value[1]


count = 0 #라벨을 만든 횟수
last_label = 0  #최종 라벨 번호
label = 0 #라벨 번호

while count < N:
     label += 1

     # 순회하는 도중에 L값이 포함되어 있지 않으면 라벨 추가
     if(str(label).find(L) < 0):
        count += 1
        last_label = label
        

print(last_label)