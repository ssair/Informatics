from random import randint
# Создание таблицы с размером 3x3, заполненной нулями

mas1 = [0] * 3

for i in range(3):
    mas1[i] = [0] * 3
print(mas1) # Выведет [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        print(mas1[i][j], end=' ')
    print()

for i in range(3):
    for j in range(3):
        mas1[i][j] = randint(0, 100)

for i in range(3):
    for j in range(3):
        print(mas1[i][j], end=' ')
    print()
print()

mas2 = [[randint(0, 100) for j in range(5)] for i in range(5)]

for i in range(5):
    for j in range(5):
        print('%2d' % (mas2[i][j]), end=' ')
    print()

print()

# Транспонирование матрицы
for i in range(5):
    for j in range(i + 1, 5):
        mas2[i][j], mas2[j][i] = mas2[j][i], mas2[i][j]

for i in range(5):
    for j in range(5):
        print('%2d' % (mas2[i][j]), end=' ')
    print()
