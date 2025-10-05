import sys
input = sys.stdin.readline

n = int(input())
child = {}
for _ in range(n):
    node, left_child, right_child = input().split()
    if not node in child:
        child[node] = []
    child[node].append(left_child)
    child[node].append(right_child)

answer = ['']*3

# 전위 순회
def preorder(cur):
    left_child, right_child = child[cur]

    answer[0] += cur
    if left_child != '.':
        preorder(left_child)
    if right_child != '.':
        preorder(right_child)

# 중위 순회
def inorder(cur):
    left_child, right_child = child[cur]

    if left_child != '.':
        inorder(left_child)
    answer[1] += cur
    if right_child != '.':
        inorder(right_child)

# 후위 순회
def postorder(cur):
    left_child, right_child = child[cur]

    if left_child != '.':
        postorder(left_child)
    if right_child != '.':
        postorder(right_child)
    answer[2] += cur

preorder('A')
inorder('A')
postorder('A')

print('\n'.join(answer))