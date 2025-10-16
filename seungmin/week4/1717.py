import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())
unf = list(range(n + 1))

def Find(target):
  if target == unf[target]:
     return target
  else:
     unf[target] = Find(unf[target])
     return unf[target]
  
def Union(a, b):
   aParent, bParent = Find(a), Find(b)

   if aParent != bParent:
      unf[aParent] = bParent

for _ in range(m):
   op, a, b = map(int, input().split())

   if op == 0:
      Union(a, b)
   elif op == 1:
      if Find(a) == Find(b):
         print("YES")
      else:
         print("NO")
