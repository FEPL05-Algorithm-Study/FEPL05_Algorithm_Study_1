from itertools import accumulate
n = int(input())
p = list(map(int, input().split()))
# 오름차순 정렬후 누적합배열 생성
p = [0] + sorted(p)
acc = list(accumulate(p))
# 누적합 배열의 총 합을 구함
print(sum(acc))