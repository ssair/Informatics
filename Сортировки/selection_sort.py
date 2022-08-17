from random import randint


def find_smallest(lst: list):
    """
    Находит наименьший элемент в списке
    """
    # Stores the smallest value
    smallest = lst[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index


def selection_sort(lst: list):
    """
    Сортировка выбором
    В этой реализации создается новый список
    и изменяется исходный
    """
    new_lst = [0]*len(lst)
    for i in range(len(lst)):
        smallest = find_smallest(lst)
        new_lst[i] = lst[smallest]
        lst.pop(smallest)
    return new_lst


random_list_of_nums = [randint(0, 20) for i in range(20)]
print(random_list_of_nums)
print(selection_sort(random_list_of_nums))


# Задание: отсортировать исходный список на месте
def selection_sort_1(lst: list):
    """
    Сортировка выбором
    Список сортируется на месте
    """
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(lst)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        lst[i], lst[lowest_value_index] = lst[lowest_value_index], lst[i]


random_list_of_nums = [randint(0, 20) for j in range(20)]
print(random_list_of_nums)
selection_sort_1(random_list_of_nums)
print(random_list_of_nums)
