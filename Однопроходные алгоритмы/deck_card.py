#
# Создаем колоду карт и перетасовываем ее
#

def create_deck():
    cards = [''] * 36
    i = 0
    for suit in ["Пик", "Крестей", "Бубей", "Червей"]:
        for value in ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]:
            cards[i] = value + ' ' + suit
            i = i + 1
    return cards


def shuffle(cards):
    from random import randrange
    for i in range(0, len(cards)):
        other_pos = randrange(i, len(cards))
        temp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = temp
    

cards = create_deck()
print("Исходная колода карт: ")
print(cards)
print()

shuffle(cards)
print("Перетасованная колода карт: ")
print(cards)

print(cards.pop())
print(cards.pop())
print(cards)