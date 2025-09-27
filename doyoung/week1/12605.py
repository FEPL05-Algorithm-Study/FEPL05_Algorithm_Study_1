import sys;

value = []

# 한줄씩 들어오는 입력값을 array로 만듬
while True:
    input = sys.stdin.readline()
    if not input:
        break

    value.append(input)

number = int(value[0])
words = [word.split() for word in value[1:]]  # 단어의 공백을 제거하고 변수에 저장

for i in range(0, number):
    words[i].reverse()   # 단어의 순서 뒤집기
    print("Case #{0}:".format(i + 1), ' '.join(words[i]))  # 다시 공백을 붙여서 제출