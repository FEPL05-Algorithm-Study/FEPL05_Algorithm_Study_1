import sys

N = int(sys.stdin.readline())

point = []

for i in range(N): 
    input = sys.stdin.readline().split()
    to_int = list(map(int, input)) # 입력값 int로 바꾸기
    run = max(to_int[0:2]) # 앞에 2개의 점수중에 높은숫자 찾기
    trick = to_int[2:] # 뒤에 5개의 숫자 저장
    trick.sort(reverse=True) # 가장 높은숫자가 앞으로 오도록 정렬
    point.append(sum(trick[0:2]) + run) # 트릭과 달리기 점수합산

print(max(point)) # 기록된 것들중 높은점수 출력
    