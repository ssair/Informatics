SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input('Слово > ').upper()
key = int(input('Ключ > '))

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        num = num + key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)
