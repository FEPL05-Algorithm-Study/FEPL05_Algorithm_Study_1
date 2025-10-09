def insertionSort(list):
  for i in range(1, len(list)):
    # j는 부분집합 S의 최대값 인덱스로 변경, why? 부분집합 S는 '항상 정렬된 상태 보장'
    j = i - 1
    # 부분집합 U의 맨 처음 값을 부분집합 S와 비교하기 위해 별도 저장
    key = list[i]

    while list[j] > key and j >= 0:
      # 부분집합 U의 첫 요소의 값 (key)보다 큰 S의 요소들을 시프트
      # 알맞은 위치에 넣을 수 있을 때까지 우로 한 칸 씩 시프트
      # 내림 차순의 경우 좌로 시프트 하겠죠?
      list[j + 1] = list[j]
      j = j - 1

    list[j + 1] = key

  return list

# def bubbleSort(list):
#   for i in range(len(list) - 1):
#     # 리스트의 길이 - 1 번 -> 패스, 각 패스마다 가장 큰 값이 뒤로 이동해야함
#     for j in range(len(list) - 1 - i):
#       # 정렬되지 않은 구간 (끝에서 i개는 이미 정렬이 보장됨)
#       if list[j] > list[j + 1]:
#           # 현재 탐색 중인 요소가 더 크다면 다음 요소와 스왑
#           list[j], list[j + 1] = list[j + 1], list[j]
  
#   return list

  

numbers = list()

for _ in range(int(input())):
  numbers.append(int(input()))

for i in insertionSort(numbers):
  print(i)
