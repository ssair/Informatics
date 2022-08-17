from random import randint


def merge(lst_a: list, lst_b: list):
    """
    Функция для слияния 2-х отсортированных списков
    """
    lst_c = [0] * (len(lst_a) + len(lst_b))
    i = k = n = 0
    while i < len(lst_a) and k < len(lst_b):
        if lst_a[i] <= lst_b[k]:
            lst_c[n] = lst_a[i]
            i += 1
            n += 1
        else:
            lst_c[n] = lst_b[k]
            k += 1
            n += 1

    while i < len(lst_a):
        lst_c[n] = lst_a[i]
        i += 1
        n += 1
    while k < len(lst_b):
        lst_c[n] = lst_b[k]
        k += 1
        n += 1

    return lst_c


def merge_sort(lst: list):
    """
    Сортировка слиянием
    """
    if len(lst) <= 1:
        return
    middle = len(lst) // 2
    lst_l = [lst[i] for i in range(0, middle)]
    lst_r = [lst[i] for i in range(middle, len(lst))]
    merge_sort(lst_l)
    merge_sort(lst_r)
    lst_c = merge(lst_l, lst_r)
    for i in range(len(lst)):
        lst[i] = lst_c[i]

a = [randint(0, 20) for i in range(20)]
print(*a)
merge_sort(a)
print(*a)