def generate_password(short_length, long_length):
    from random import randint
    MIN_ASCII = 33
    MAX_ASCII = 126

    random_length = randint(short_length, long_length)

    result = ""
    for i in range(random_length):
        random_char = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + random_char

    return result


print(generate_password(1, 3))
