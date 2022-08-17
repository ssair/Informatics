from random import randint


def bubble_sort(lst: list):
    """
    Сортировка методом пузырька
    """
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                # Меняем элементы
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


random_list_of_nums = [randint(0, 20) for i in range(20)]
print(random_list_of_nums)
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
