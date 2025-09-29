questions = [input() for _ in range(int(input()))]

for question in questions:
    if(type(question) == str):
        print(f'Case #{questions.index(question)+1}: {' '.join(list(question.split(' '))[::-1])}')

