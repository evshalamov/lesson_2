element = int(input('Введите количество элементов: '))
numb = []
i = 0
a = 0
while i < element:
    numb.append(input('Введите элемент: '))
    i += 1

for b in range(1, len(numb), 2):
        numb[a], numb[a + 1] = numb[a + 1], numb[a]
        a += 2
print(numb)