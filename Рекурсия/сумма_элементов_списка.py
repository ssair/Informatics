def sum_list(lst: list):
    """
    Считает сумму элементов списка реккурентно
    """
    s = 0
    if len(lst) < 2:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])   # или lst.pop(0) + sum_list(lst)


a = [2, 4, 6]
print(sum_list(a))
