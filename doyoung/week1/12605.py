import sys;

value = []

while True:
    input = sys.stdin.readline()
    if not input:
        break

    value.append(input)

number = int(value[0])
words = [word.split() for word in value[1:]] 

for i in range(0, number):
    words[i].reverse()
    print("Case #{0}:".format(i + 1), ' '.join(words[i]))