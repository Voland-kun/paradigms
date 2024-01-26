from random import randint

def coinflip():
    player_count = randint(0, 1)
    print('Бросок монеты:')
    if player_count == 1:
        print(f'Выпала решка, первым ходит {players[(player_count)%2]}')
    else:
        print(f'Выпал орёл, первым ходит {players[(player_count)%2]}')
    return player_count

player1 = 'Игрок1'
player2 = 'Игрок2'
players = [player1, player2]
field_visual = ['___|','___|','___','___|','___|','___','   |','   |','   ']
field_visual = [(field_visual[_][:1] + str(_+1) + field_visual[_][2:]) for _ in range(9)]
field = ['' for _ in range(9)]
player_count = coinflip()
char = 'XO'

def vis(field_visual):
    for i in range(3):
        for j in range(3):
            print(field_visual[i*3+j], end= '')
        print()

def win_condition(field):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i in win_conditions:
        if field[i[0]] == field[i[1]] == field[i[2]] != '':
            win_flag = True
            break
        else:
            win_flag = False
    return win_flag

def player_input(players, player_count):
    while True:
        move = input(f'Ходит {players[player_count%2]}. Выберите поле: ')
        try:
            move = int(move)
        except:
            print('Введите номер клетки (число от 1 до 9')
            continue
        if 0 < move < 10:
            if (field[move-1] != ''):
                print('Эта клетка занята.')
            else:
                field[move-1] = char[player_count%2]
                break
        else:
            print('Введите номер клетки (число от 1 до 9')
    return move

def tictactoe(field, field_visual, player_count, players, char):
    count = 0
    vis(field_visual)
    while True:
        move = player_input(players, player_count)
        field[move-1] = char[count%2]
        field_visual[move-1] = field_visual[move-1][:1] + field[move-1] + field_visual[move-1][2:]
        vis(field_visual)
        count += 1
        if count >= 4:
            if win_condition(field):
                print(f'Победил {players[player_count%2]}.')
                break
        if count >= 9:
            print('Ничья.')
            break
        player_count += 1


tictactoe(field, field_visual, player_count, players, char)
input('Press enter to exit\n')
