# В этой реализации создается новый список
# и изменяется исходный
# Задание: отсортировать исходный список на месте

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


def selectionSort(arr):
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

print(selectionSort([5, 3, 6, 2, 14]))
