n, l = map(int, input().split())
target = 1
labelCount = 0

while True:
  # 가능한 수의 갯수가 언제 n에 도달할지 모르므로 while문을 사용.
  if str(l) not in str(target):
    # l이 target 수에 포함이 되어있지 않은, 라벨링 가능한 수라면
    # labelCount 1 증가
    labelCount += 1
    if labelCount == n:
      # 라벨링한 카운트가 n에 도달하면 해당 타겟 수를 출력하고 반복 종료
      print(target)
      break
    target += 1
  else:
    # 라벨링 가능한 수가 아니라면 타겟 수만 증가
    target += 1
