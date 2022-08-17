from random import randint


def counting_sort(lst, min_nums, max_nums):
    count_lst = [0] * len(lst)
    for i in lst:
        count_lst[i] += 1
    result_lst = []

    for j in range(min_nums, max_nums + 1):
        result_lst += [j] * count_lst[j]

    return result_lst


a = [randint(0, 5) for i in range(21)]
print(*a)
b = counting_sort(a, 0, 20)
print(*b)
