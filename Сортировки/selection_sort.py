# Сортировка выбором
# В этой реализации создается новый список
# и изменяется исходный

def find_smallest(arr):
    """
    Finds the smallest value in an array
    """
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """
    Sort array
    """
    new_arr = [0]*len(arr)
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr)
        new_arr[i] = arr[smallest]
        arr.pop(smallest)
    return new_arr

# print(selection_sort([5, 3, 6, 2, 14]))


# Задание: отсортировать исходный список на месте
def selection_sort_1(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


nums = [5, 3, 6, 2, 14]
selection_sort_1(nums)
print(nums)