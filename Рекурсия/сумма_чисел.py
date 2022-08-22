def sum_nums(n):
    """
    Сумма чисел от 1 до n
    """
    if n < 2:
        return 1
    else:
        return n + sum_nums(n-1)
