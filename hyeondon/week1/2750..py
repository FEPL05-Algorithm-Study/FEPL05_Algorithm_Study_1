import sys

n = int(sys.stdin.readline())
bubbleArray = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(len(bubbleArray)-1) : 
    for j in range(len(bubbleArray)-1-i) : 
      if bubbleArray[j] > bubbleArray[j+1] : 
        temp = bubbleArray[j] 
        bubbleArray[j] = bubbleArray[j+1] 
        bubbleArray[j+1] = temp

print(bubbleArray)
