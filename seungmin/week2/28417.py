winner = 0

for _ in range(int(input())):
  scores = list(map(int, input().split()))
  run, trick = scores[:2], scores[2:]

  run.sort(reverse=True)
  trick.sort(reverse=True)

  winner = max(winner, (run[0] + trick[0] + trick[1]))

print(winner)
