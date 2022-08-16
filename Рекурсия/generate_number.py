def generate_bin(M:int, prefix=""):
    """
        Генерирует все числа (с лидирующими незначащами нулями)
        в 2-ичной системе счисления
        длины M
        """
    if M == 0:
        print(prefix)
        return
    generate_bin(M-1, prefix + "0")
    generate_bin(M-1, prefix + "1")


def generate_number(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащами нулями)
    в N-ричной системе счисления (N <= 10)
    длины M
    """
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep="")
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


# только для двоичной СС
generate_bin(5)

# для произвольной СС
generate_number(4, 3)