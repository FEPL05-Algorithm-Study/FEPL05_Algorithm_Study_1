import sys

input = sys.stdin.readline

t = int(input())

a = t // 300
b = t % 300 // 60
c = t % 300 % 60 // 10

if (a * 300) + (b * 60) + (c * 10) != t:
  print(-1)
else:
  print(a, b, c)
