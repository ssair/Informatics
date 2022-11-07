def prim_div(n):
    """
    Раскладывает число на простые множители
    """
    i = 2
    prim = []
    while i * i <= n:
        while n % i == 0:
            prim.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prim.append(n)
    return prim


print(prim_div(2))
