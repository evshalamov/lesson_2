words = input('Введите несколько слов через пробел: ')
word = []
a = 1
for i in range(words.count(' ') + 1):
    word = words.split()
    if len(str(word)) <= 10:
        print(f' {a} {word [i]}')
    else:
        print(f' {a} - {word [i] [0:10]}')
        a += 1