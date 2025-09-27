n = int(input())
cards = list(map(int,input().split(' ')))
m = int(input())
nums = list(map(int,input().split(' ')))

s = set()
for i in range(n):
    s.add(cards[i])

answer = [0]*m
for i in range(m):
    answer[i] = int(nums[i] in s)

print(' '.join(map(str,answer)))
