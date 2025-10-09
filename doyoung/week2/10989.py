import sys

N = int(sys.stdin.readline()) # 첫행이 의미하는 데이터 갯수 받기

value = {}

for i in range(N):
    input = sys.stdin.readline()

    # 딕셔너리에 키가 없으면 1로 초기화, 있으면 +1
    if not int(input) in value.keys():
        value[int(input)] = 1
    else:
        value[int(input)] += 1


# 키를 오름차순으로 정렬 후, value의 갯수만큼 출력
for i in sorted(value.keys()):
    for j in range(value[i]):
        print(i)