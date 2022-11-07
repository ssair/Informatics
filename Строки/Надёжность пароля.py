def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    is_len = False
    # Проверяем каждый символ в пароле
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True

    if len(password) >= 8:
        is_len = True

    return int(has_upper) + int(has_lower) + int(has_num) + int(is_len)


print(check_password("AAA"))
