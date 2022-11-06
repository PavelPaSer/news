
from cgitb import text
import emoji as em
from progress.bar import ChargingBar
import time 
from emoji import emojize as emo


board = list(range(1, 10))

winner_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3 ,6 ,9), (1, 5, 9), (3, 5, 7)]


print('Крестики-нолики')
print()
time.sleep(1)
print(f'Дорогие друзья! Пока грузится игра ознакомтесь с правилами игры.\n'
        'Сначала делает ход первый игрок, (решите заранее кто играет за X и O) \n'
        'Продолжайте обмениваться ходами до тех пор, пока один из игроков не начертит\n'
        'три символа в один ряд или пока не наступит ничья\n')
bar = ChargingBar('Идет загрузка...', max = 8)
for i in range(8):
    time.sleep(1)
    # Do some work
    bar.next()
bar.finish()



def get_game(num: int):
    return [x for x in range(1, num * num + 1)]


def markup(lis: list):
    print('-' * 19)
    for i in range(3):
        print(\
            f'|  {lis[0 + i * 3]}  |  {lis[1 + i *3]}  |  {lis[2 + i * 3]}  |')
        print('-' * 19)


def get_input(game_board, player):
    flag = False
    while not flag:
        try:
            player_input = int(input(f'Ход игрока с {player} : '))
        except:
            print('Введите свободное число')
            continue
        if player_input >= 1 and player_input <= 9:
            if not em.is_emoji(game_board[player_input - 1]):
                game_board[player_input - 1] = player
                flag = True
            else:
                print('Клетка уже занята! Повторите попытку снова')
        else:
            print('Не корректный ввод, введите число от 1 до 9 .')


def check_board(board: list):
    vin_cod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))
    for item in vin_cod:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False


def start_game():
    count_ = 0
    flag = False
    game_board = get_game(3)
    while not flag:
        markup(game_board)
        if count_ % 2 == 0:
            char = f'{emo(":multiply:")}' 
        else:
            char = f'{emo(":hollow_red_circle:")}'
        get_input(game_board, char)
        count_ += 1
        if count_ >= 5:
            temp = check_board(game_board)
            if temp:
                print(f'\nУра! Победил игрок с {temp}\n')
                flag = True
                break
        if count_ == 9:
            print('Ничья!')
            break
    markup(game_board)

start_game()
