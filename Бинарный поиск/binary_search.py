def binary_search(lst, item):
  """
  Бинарный поиск элемента в списке
  Возвращает индекс элемента (первого, если их несколько)
  и None, если его в списке нет
  """
  # Нижняя и верхняя граница в поиске
  low = 0
  high = len(lst) - 1

  # Пока вы не сузили список до одного элемента ...
  while low <= high:
    # ... вычисляем индекс среднего элемента
    mid = (low + high) // 2
    guess = lst[mid]
    # Если элемент найден ...
    if guess == item:
      return mid
    # Если элемент элемент больше среднего
    if guess > item:
      high = mid - 1
    # Если элемент элемент меньше среднего
    else:
      low = mid + 1

  # Элемент не найден
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

print(binary_search(my_list, -1)) # => None
