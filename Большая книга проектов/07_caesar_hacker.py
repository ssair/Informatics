print('Введите зашифрованную строку')
message = input('> ').upper()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            # Если символа нет в алфавите, добавляем его как есть
            translated = translated + symbol

    print('Key #', key,'-', translated)
