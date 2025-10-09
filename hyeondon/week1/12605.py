import sys

count = int(sys.stdin.readline()) 
wordList = []

for i in range(1, count+1):   # 1부터 시작
    word = sys.stdin.readline().rstrip()
    if ' ' in word:
        reversedWord = " ".join(word.split()[::-1])
        wordList.append(reversedWord)
    else:
        wordList.append(word)

    print(f'Case #{i}: {wordList[-1]}')
