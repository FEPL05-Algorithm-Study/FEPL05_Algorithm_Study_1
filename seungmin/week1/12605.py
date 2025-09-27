for i in range(int(input())):
  l = list(map(str, input().split()))
  print(f"Case #{i+1}: {' '.join(l[::-1])}")
