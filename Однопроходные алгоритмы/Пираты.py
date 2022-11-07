flag = 0
a = 0
while flag == 0:
    a += 1
    if a % 2 == 1 and a % 3 == 1 \
            and a % 4 == 1 and a % 5 == 1 \
            and a % 6 == 1 and a % 7 == 0:
        flag = 1


print(a)