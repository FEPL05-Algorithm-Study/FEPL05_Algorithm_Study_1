import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (4 * n)

# 세그먼트 트리 초기화
def init(arr, tree, node, start, end):
  # 노드가 리프 노드인 경우 
  # e. g. [start, end] => [1, 1]인 경우
  if start == end:
    tree[node] = arr[start]
    return tree[node]
  
  # 현재 노드가 담당하는 구간을 정확히 반으로 나눔
  # start ~ mid : 왼쪽 자식, mid + 1 ~ end: 오른쪽 자식
  mid = (start + end) // 2

  tree[node] = init(arr, tree, node * 2, start, mid) + init(arr, tree, node * 2 + 1, mid + 1, end)
  
  return tree[node]

# 구간합 구하기
def prefixSum(tree, node, start, end, left, right):
  # [left, right]의 구간합을 구한다.

  # [start, end] 앞 뒤에 [left, right]가 있는 경우 겹치지 않으므로 탐색할 필요가 없다.
  # [start, end] : 현재 노드가 포함하는 구간
  if left > end or right < start : 
    return 0
  
  #[start, end]가 [left, right]에 포함되는 경우
  if left <= start and end <= right:
    return tree[node]
  
  # 일부만 겹치는 경우 왼쪽 자식과 오른쪽 자식을 루트로 하는 하위 트리에서 재탐색
  mid = (start + end) // 2

  prefix = prefixSum(tree, node * 2, start, mid, left, right) + prefixSum(tree, node * 2 + 1, mid + 1, end, left, right)

  return prefix

# 구간합 갱신
def update(tree, node, start, end, index, diff):
  # 현재 노드의 구간이 인덱스를 포함하지 않는다면 해당 하위 트리로 내려갈 필요가 없다.
  if index < start or index > end:
    return
  
  # 해당하면 차 만큼만 더해주면 된다.
  tree[node] = tree[node] + diff

  if start != end:
    mid = (start+ end) // 2
    # 왼쪽 자식, 오른쪽 자식 갱신
    update(tree, node * 2, start, mid, index, diff)
    update(tree, node * 2 + 1, mid + 1, end, index, diff)

  


for i in range(1, n + 1):
  arr[i] = int(input())

# 세그먼트 트리 초기화
init(arr, tree, 1, 1, n)

for _ in range(m + k):
  a, b, c = map(int, input().split())

  if a == 1:
    # a가 1이면 갱신 (update)
    diff = c - arr[b]
    arr[b] = c
    update(tree, 1, 1, n, b, diff)
  elif a == 2:
    print(prefixSum(tree, 1, 1, n, b, c))



