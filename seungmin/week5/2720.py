import sys

input = sys.stdin.readline

quarter = 25
dime = 10
nickel = 5
penny = 1

for _ in range(int(input())):
  c = int(input())
  q = c // quarter
  d = c % quarter // dime
  n = c % quarter % dime // nickel
  p = c % quarter % dime % nickel // penny
  print(q, d, n, p)
