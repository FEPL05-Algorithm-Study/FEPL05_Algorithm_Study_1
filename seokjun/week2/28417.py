n = int(input())
arr = [list(map(int,input().split(' '))) for _ in range(n)]

scores = []
for x in arr:
    score = x[0] if x[0]>x[1] else x[1]
    trick = x[2:]
    trick.sort(reverse=True)
    score += trick[0] + trick[1] 
    scores.append(score)

scores.sort(reverse=True)

print(scores[0])