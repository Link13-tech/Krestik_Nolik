print("---------------------------------------------------------------------------------------------------------------")
print("Доброго времени суток!\nЕсли вы устали от GTA и Counter-strike\nТолько сегодня у вас есть возможность сыграть \
в...\nКРЕСТИКИ - НОЛИКИ")
print("")
print("Для начала немного правил:\n1.Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики,\
другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигр\
ывает.\n2.Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали \n\
нет трёх одинаковых знаков, партия считается закончившейся в ничью. Первый ход делает игрок, ставящий крестики. ")
print("---------------------------------------------------------------------------------------------------------------")


def my_board(board):                                                # создание поля'
    print("  0 1 2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=" ")
        print()


def init_board():                                                  # заполнение поля "-"
    return [['-' for _ in range(3)] for _ in range(3)]


game_board = init_board()


def step(board, move, i, j):                                       # ход
    if 0 <= i <= 2 and 0 <= j <= 2 and board[i][j] == '-':
        board[i][j] = move
        return True
    else:
        print("Неверный ход. Попробуй еще.")
        return False


def check_draw(board):                                             # проверка ничьи
    for i in board:
        for value in i:
            if value in ['-']:
                return False
    return True


def check_winner(board):                                           # проверка выигрыша
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-' or board[0][i] == board[1][i] == board[2][i] != '-':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '-' or board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    return False


def game():                                                        # ввод, проверка на цифры
    player = 'x'
    while not check_winner(game_board) and not check_draw(game_board):
        print('**********************************')
        my_board(game_board)
        try:
            i = int(input(f"{player}, выберите номер строки  (0-2): "))
        except (TypeError, ValueError):
            print("Нужно ввести цифру)")
            continue
        try:
            j = int(input(f"{player}, выберите номер столбца (0-2): "))
        except (TypeError, ValueError):
            print("Нужно ввести цифру)")
            continue
        if step(game_board, player, i, j):
            if check_winner(game_board):
                print('**********************************')
                my_board(game_board)
                print(f"Игрок {player} победил! Поздравляю")
                break
            elif check_draw(game_board):
                print('**********************************')
                my_board(game_board)
                print("Ничья! Нужно потренероваться")
                break
            else:
                player = 'o' if player == 'x' else 'x'
        else:
            continue


game()
