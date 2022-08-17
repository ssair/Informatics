# Сортировка методом пузырька

def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                # Меняем элементы
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
# Проверяем, что оно работает
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
