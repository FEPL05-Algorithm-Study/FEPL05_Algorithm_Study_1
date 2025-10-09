import sys

input = sys.stdin.readline

numbers = list()

for _ in range(int(input())):
  numbers.append(int(input()))

numbers.sort()

for num in numbers:
  print(num)
