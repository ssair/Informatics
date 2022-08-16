def find_number_in_prefix(number, A):
    """
    Ищет number в A и возвращает True, если такой есть
    и False, если такого нет
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_permutations(N:int, M:int=-1, prefix=None):
    """
    Генерирация всех перестановок N в M позициях
    с префиксом prefix
    """
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find_number_in_prefix(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(4, 3)