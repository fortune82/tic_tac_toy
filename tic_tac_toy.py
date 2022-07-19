import time  # для создания эффекта печатания текста с задержкой
# для созлания разноцветного текста в программе
from colorama import init, Fore, Back, Style
init()

print(Style.BRIGHT + Fore.YELLOW)
wordTitle = """Правила игры ! 
Игроки по очереди ставят на свободные клетки поля знаки (один всегда крестики, другой всегда нолики). 
Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает."""


for i in wordTitle:
    # print(Style.BRIGHT + Fore.YELLOW)
    print(i, end="")
    time.sleep(0.02)

# в эту переменную записываем чем будет играть первый игрок ('X' или 'O')
player1 = ""
player2 = ""


# Пользователь выбирает чем будет играть ('X' или 'O'). Если пользователь выбрал неправилный символ, тогда запускаем повторно эту функциию, иначе запускаем функцию с отрисовокой


def player_choose():
    print(Style.BRIGHT + Fore.GREEN)
    global player1
    global player2
    print()
    player1 = input(
        "\nПожалуйста выберите символ 'X' или 'O' на английском языке:  ")
    # set_symbols = ["x", "X", "o", "O", "х", "Х", "О", "о"]
    set_symbols = ["x", "o"]
    if player1 in set_symbols:
        if player1 == 'x':
            player2 = "o"
        else:
            player1 == "o"
            player2 = "x"
    else:
        print(" Вы ввели неправльный символ. Попробуйте ещё раз! ")
        player_choose()


player_choose()

player = [player1, player2]

# запускаем отрисовку поля

# board = range(0, 10) . Поле из 9 ячеек
board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

""" Отрисовываем поле """


def board_draw(board):
    # print(Style.BRIGHT + Fore.RED)
    print(board[1], "|", board[2], "|", board[3])
    print("----------")
    print(board[4], "|", board[5], "|", board[6])
    print("----------")
    print(board[7], "|", board[8], "|", board[9])


board_draw(board)

num_x = []  # массив для х
num_o = []  # массив для о

# запуск игры


def square_num(player):
    global board
    global num_x
    global num_o
    # strikethrough = []
    # чтобы поочередно менять игроков (х на о) проходим функцию два раза и повторно запускае её
    for i in range(len(player)):
        # присваиваем playerNew (в зависимости от того какой это проход for i in range(len(player))  либо player[i] = "х" либо player[i] = "о")
        playerNew = player[i]
        # print(i)
        choose_num = int(input(" Введите число от 1 до 9 если оно не занято "))

        for i in range(1, 10):  # перебираем 9 клеток
            # проверяем занята ли клетка
            if choose_num in num_x or choose_num in num_o:
                print("Эта клетка занята")
                square_num(player)
            # если клетка свободна, тогда добавляем цифру (клетку) в массив num_x или num_o = []
            elif choose_num == i:
                # если пользователь выбрал "х", тогда добавляем число в массив num_x и рисуем "х"
                if playerNew == 'x':
                    num_x.append(i)
                    board[i] = 'x'  # заменяем цифру на символ
                    board_draw(board)
                    # проверяем выйгрышную комбинацию
                    if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]) or (board[7] == board[4] == board[1]) or (board[8] == board[5] == board[2]) or (board[9] == board[6] == board[3]):
                        board[i] = 'x'  # заменяем цифру на символ
                        print(" Поздравляем!!! Крестики выйграли!!!  ")
                        num_x = []  # обнуляем массив для х
                        num_o = []  # обнуляем массив для о
                        # возвращаем первоначальный массив
                        board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        player_choose()
                    break
                elif playerNew == 'o':
                    # если пользователь выбрал "o", тогда добавляем число в массив num_o и рисуем "o"
                    num_o.append(i)
                    board[i] = 'o'  # заменяем цифру на символ
                    board_draw(board)
                    if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]) or (board[7] == board[4] == board[1]) or (board[8] == board[5] == board[2]) or (board[9] == board[6] == board[3]):
                        board[i] = 'o'  # заменяем цифру на символ
                        print(" Поздравляем!!!Нолики выйграли!!!  ")
                        num_x = []  # обнуляем массив для х
                        num_o = []  # обнуляем массив для о
                        # возвращаем первоначальный массив
                        board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                        player_choose()
                    break
    square_num(player)


square_num(player)
