# 라벨이 있는데, 양의 정수로 된 라벨 
# N과 L이 주어짐 
# 이 때 L이 N에 포함되면 안됨 숫자 자체가 

import sys

N, L = map(int, sys.stdin.readline().split())
totalList = []

for i in range(1, 10**7):
    if str(L) not in str(i) and len(totalList) < N :   # 핵심 수정
        totalList.append(i)

print(totalList[-1])
