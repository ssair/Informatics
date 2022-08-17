from random import randint


def insertion_sort(lst: list):
    """
    Сортировка вставками
    """
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        # Вставляем элемент
        lst[j + 1] = item_to_insert


# Проверяем, что оно работает
random_list_of_nums = [randint(0, 20) for i in range(20)]
print(random_list_of_nums)
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
