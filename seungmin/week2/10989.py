import sys

input = sys.stdin.readline
numbers=[0] * 10001

for _ in range(int(input())):
  num = int(input())
  numbers[num] += 1

for i in range(10001):
    if numbers[i] > 0:
        for _ in range(numbers[i]):
            print(i)
