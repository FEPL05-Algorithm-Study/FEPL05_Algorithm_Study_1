n = int(input())
cards = list(map(int,input().split(' ')))
m = int(input())
nums = list(map(int,input().split(' ')))

s = set(cards)
answer = []
for i in range(m):
    answer.append(int(nums[i] in s))

print(' '.join(map(str,answer)))
