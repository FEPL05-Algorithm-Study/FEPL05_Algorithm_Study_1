import sys

lines = sys.stdin.read().split('\n')
arr = list(map(int, lines[1:]))
arr.sort()

for item in arr:
    print(item)


