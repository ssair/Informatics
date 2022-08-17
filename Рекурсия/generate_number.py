def generate_bin(length_bin: int, prefix=""):
    """
        Генерирует все числа (с лидирующими незначащами нулями)
        в 2-ичной системе счисления
        длины length_bin
        """
    if length_bin == 0:
        print(prefix)
        return
    generate_bin(length_bin - 1, prefix + "0")
    generate_bin(length_bin - 1, prefix + "1")


def generate_number(number_system: int, length_number: int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащами нулями)
    в number_system-ричной системе счисления (number_system <= 10)
    длины length_number
    """
    prefix = prefix or []
    if length_number == 0:
        print(*prefix, sep="")
        return
    for digit in range(number_system):
        prefix.append(digit)
        generate_number(number_system, length_number - 1, prefix)
        prefix.pop()


# только для двоичной СС
generate_bin(5)

# для произвольной СС
generate_number(4, 3)
