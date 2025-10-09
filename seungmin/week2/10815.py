import sys
import bisect # 이진 탐색을 도와주는 표준 라이브러리

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

m = int(input())
targets = list(map(int, input().split()))
ans = list()

for target in targets:
  # 이진 탐색 진행
  # numbers에 target이 있는지 확인
  idx = bisect.bisect_left(numbers, target)
  if idx < len(numbers) and numbers[idx] == target:
    ans.append(1)
  else:
    ans.append(0)

print(" ".join(map(str, ans)))
