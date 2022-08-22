# https://habr.com/ru/company/otus/blog/529356/?ysclid=l72w9jk8k9603170540

import itertools

s = "12345"
lst_itertools = itertools.product(s, repeat=5)
lst = list(lst_itertools)
count = 0
for e in lst:
    if e.count("1") == 3:
        count += 1
print(count)

s = "ЛЕВИЙ"
lst_itertools = itertools.permutations(s, 5)
lst = list(lst_itertools)

count = 0
for e in lst:
    flag = True

    for i in range(len(e) - 1):
        if e[0] == "Й" or e[i] == "Е" and e[i+1] == "И":
            flag = False
    if flag:
        count += 1
print(count)
