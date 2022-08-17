from random import randint


def counting_sort(array, mn, mx):
    count = [0] * len(array)

    for i in array:
        count[i] += 1

    result = []

    for j in range(mn, mx + 1):
        result += [j] * count[j]

    return result


a = [randint(0, 20) for i in range(21)]
print(*a)
b = counting_sort(a, 0, 20)
print(*b)
