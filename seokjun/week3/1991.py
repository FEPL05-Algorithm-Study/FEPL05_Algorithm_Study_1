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


# 전위 순회
def preorder(cur):
    if cur != '.':
        left_child, right_child = child[cur]
        print(cur,end='')
        preorder(left_child)
        preorder(right_child)

# 중위 순회
def inorder(cur):
    if cur != '.':
        left_child, right_child = child[cur]
        inorder(left_child)
        print(cur,end='')
        inorder(right_child)

# 후위 순회
def postorder(cur):
    if cur != '.':
        left_child, right_child = child[cur]
        postorder(left_child)
        postorder(right_child)
        print(cur,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')