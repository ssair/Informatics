def find_number_in_prefix(number: int, lst: list):
    """
    Ищет number в lst и возвращает True, если такой есть
    и False, если такого нет
    """
    flag = False
    for x in lst:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(number: int, length_number: int = -1, prefix=None):
    """
    Генерирация всех перестановок number в length_number позициях
    с префиксом prefix
    """
    # по умолчанию number чисел в number позициях
    length_number = number if length_number == -1 else length_number
    prefix = prefix or []
    if length_number == 0:
        print(prefix)
        return
    for digit in range(1, number + 1):
        if find_number_in_prefix(digit, prefix):
            continue
        prefix.append(digit)
        generate_permutations(digit, length_number - 1, prefix)
        prefix.pop()


generate_permutations(4, 3)
