import sys

input = sys.stdin.readline
tree = {}

def preorder(root):
  # 전위 순회 - 루, 왼, 오
  if root != '.':
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
  # 중위 순회 - 왼, 루, 오
  if root != '.':
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
  # 후위 순회 - 왼, 오, 루
  if root != '.':
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')


for i in range(int(input())):
  root, left, right = map(str, input().split())
  tree[root] = left, right

preorder('A')
print()
inorder('A')
print()
postorder('A')
