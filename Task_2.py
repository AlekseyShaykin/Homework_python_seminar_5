

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


import random

participant = ['me', 'opponent']
move = random.choice(participant)
print(move)

candy_numbers = 21
range = 3


# автоматический расчет первого хода ЧЕЛОВЕКА даже с учетом того, что первый ход за БОТом
def My_first_move(candy_numbers, range, bot_first_move):
    first_move = (candy_numbers-bot_first_move) - \
        (((candy_numbers-bot_first_move)//(range+1)))*(range+1)
    return first_move


def Check_bot(increm, move, total_candies):              # проверка на перелимит БОТА
    print(f'increment = {increm}')
    if increm == total_candies:
        print("Бот победил!")
        exit()
    elif increm > total_candies:
        print(f'Бот, введите меньшее кол-во конфет: ', end=" ")
        y = random.randint(1, (total_candies-(increm-move)))
        print(y)
        if (increm-move+y) == total_candies:
            print("Бот победил!")
            exit()
        return y


def Check_Man(increm, total_candies):              # проверка на победный ход ЧЕЛОВЕК
    print(f'increment = {increm}')
    if (increm) == total_candies:
        print('ЧЕЛОВЕК ПОБЕДИЛ!')
        exit()


first = My_first_move(candy_numbers, range, 0)
print(f"Первому игроку нужно взять {first} конфет")


if move == 'me':
    print(f'ХОД №1. Количество конфет первого хода: {first}')
    count = 2
    increm = first
    while increm < candy_numbers:
        print(f'ХОД №{count}.Бот, введите количество конфет: ', end=" ")
        y = random.randint(1, range)
        print(y)
        increm += y

        Check_bot(increm, y, candy_numbers)
        # print(f"TTT = {c}")
        print(f'ХОД №{count+1}', end=' ')
        x = int(input('Человек, введи количество конфет: '))
        increm = increm+x
        Check_Man(increm, candy_numbers)
        count += 2
else:
    print('ХОД №1. Бот, введите количество конфет: ', end=" ")
    y = random.randint(1, range)
    print(y)
    count = 2
    first = My_first_move(candy_numbers, range, y)
    print(f"ХОД №{count} Человек, введи количество конфет: {first} ")
    increm = first+y

    while increm < candy_numbers:
        print(f'ХОД №{count}.Бот, введите количество конфет: ', end=" ")
        y = random.randint(1, range)
        print(y)
        increm += y

        Check_bot(increm, y, candy_numbers)
        # print(f"TTT = {c}")
        print(f'ХОД №{count+1}', end=' ')
        x = int(input('Человек, введи количество конфет: '))
        increm = increm+x
        Check_Man(increm, candy_numbers)
        count += 2