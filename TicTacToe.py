#! python3 Gra Kółko i krzyżyk dla dwóch graczy
import pyfiglet


board01 = [[' ', '|', ' ', '|', ' '],
           ['-----'],
           [' ', '|', ' ', '|', ' '],
           ['-----'],
           [' ', '|', ' ', '|', ' ']]

board02 = [['7', '|', '8', '|', '9'],
           ['-----'],
           ['4', '|', '5', '|', '6'],
           ['-----'],
           ['1', '|', '2', '|', '3']]


def print_board(board):
    for i in board:
        print(''.join(i))


def prompt():
    x = ''
    while x != 'o' or x != 'x':
        x = input('Wybierz czy chcesz grać "X" czy "O":')
        if x.lower() == 'x':
            return 'X'
        elif x.lower() == 'o':
            return 'O'
        else:
            print(f'Wybrałeś {x}, a nie "X" lub "O". Spróbuj raz jeszcze')


letter = prompt()


def pole():
    if letter == 'X':
        return 'xoxoxoxoxo'
    elif letter == 'O':
        return 'oxoxoxoxox'


def check():
    x = pyfiglet.figlet_format("WYGRANA !!!")
    if board01[0][0] == board01[0][2] and board01[0][2] == board01[0][4] and board01[0][0] != ' ':
        print(x)
    elif board01[2][0] == board01[2][2] and board01[2][2] == board01[2][4] and board01[2][0] != ' ':
        print(x)
    elif board01[4][0] == board01[4][2] and board01[4][2] == board01[4][4] and board01[4][0] != ' ':
        print(x)
    elif board01[0][0] == board01[2][0] and board01[2][0] == board01[4][0] and board01[0][0] != ' ':
        print(x)
    elif board01[0][2] == board01[2][2] and board01[2][2] == board01[4][2] and board01[0][2] != ' ':
        print(x)
    elif board01[0][4] == board01[2][4] and board01[2][4] == board01[4][4] and board01[0][4] != ' ':
        print(x)
    elif board01[0][0] == board01[2][2] and board01[2][2] == board01[4][4] and board01[0][0] != ' ':
        print(x)
    elif board01[0][4] == board01[2][2] and board01[2][2] == board01[4][0] and board01[0][4] != ' ':
        print(x)
    else:
        pass


print_board(board02)

for i in pole():
    x = input('Wybierz numer pola GRACZU: ')
    if x == '7':
        board01[0][0] = i.upper()
        print_board(board01)
        check()
    elif x == '8':
        board01[0][2] = i.upper()
        print_board(board01)
        check()
    elif x == '9':
        board01[0][4] = i.upper()
        print_board(board01)
        check()
    elif x == '4':
        board01[2][0] = i.upper()
        print_board(board01)
        check()
    elif x == '5':
        board01[2][2] = i.upper()
        print_board(board01)
        check()
    elif x == '6':
        board01[2][4] = i.upper()
        print_board(board01)
        check()
    elif x == '1':
        board01[4][0] = i.upper()
        print_board(board01)
        check()
    elif x == '2':
        board01[4][2] = i.upper()
        print_board(board01)
        check()
    elif x == '3':
        board01[4][4] = i.upper()
        print_board(board01)
        check()
    else:
        break
