# Выводим памятку для игроков
print('Нумерация клеток игрового поля:')
print(' 1' + ' |' + ' 2' + ' |' + ' 3')
print('---+---+---')
print(' 4' + ' |' + ' 5' + ' |' + ' 6')
print('---+---+---')
print(' 7' + ' |' + ' 8' + ' |' + ' 9' "\n")
print('Игра началась.')

# Создаем элементы стартового игрового поля
game_field = {'1': ' ', '2': ' ', '3': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '7': ' ', '8': ' ', '9': ' '}

field_keys = []

for key in game_field:
    field_keys.append(key)


# Рисуем игровое поле
def print_game_field(field):
    print(' ' + field['1'] + ' | ' + field['2'] + ' | ' + field['3'])
    print('---+---+---')
    print(' ' + field['4'] + ' | ' + field['5'] + ' | ' + field['6'])
    print('---+---+---')
    print(' ' + field['7'] + ' | ' + field['8'] + ' | ' + field['9'])


# Задаем условия для победы
def victory(game_field_vic):
    vict = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9'],
            ['1', '5', '9'],
            ['3', '5', '7']]
    for n in vict:
        if all(game_field_vic[y] == 'X' for y in n) or all(game_field_vic[y] == '0' for y in n):
            return True
    return False


# Реализуем игровой процесс.
def game():
    player = 'X'
    count = 0

    for i in range(1, 10):
        print_game_field(game_field)
        print('Ходит игрок ' + player + '. Введите номер клетки на игровом поле: ')
        turn = input()
        if turn in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if game_field[turn] == ' ':
                game_field[turn] = player
                count += 1
            else:
                print('Это поле уже занято.\nВведите номер другой клетки.')
                continue
        else:
            print('Некорректное значение.\nДолжно быть число от 1 до 9.')
            continue

        # По достижении пятого хода начинаем проверять выполнение условий победы.
        if count >= 5:
            if victory(game_field):
                print_game_field(game_field)
                print('\nИгра завершена.\n')
                print(' **** Победил игрок ' + player + ' . ****')
                break

        # Если ни X, ни 0 не победили, а поле уже заполнено, объявляется ничья.
        if count == 9:
            print_game_field(game_field)
            print("\nИгра завершена.\n")
            print("Ничья.")

        # Передаем ход другому игроку после каждого хода.
        if player == 'X':
            player = '0'
        else:
            player = 'X'


game()
