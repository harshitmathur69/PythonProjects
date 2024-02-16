#Step - 1
#Display the game board
def display_board(board):
    print('    | '+'  | ')
    print('  '+board[7]+' | '+board[8]+' | '+board[9])
    print('    | '+'  | ')
    print('---'+'---'+'-------')
    print('    | '+'  | ')
    print('  '+board[4]+' | '+board[5]+' | '+board[6])
    print('    | '+'  | ')
    print('---'+'---'+'-------')
    print('    | '+'  | ')
    print('  '+board[1]+' | '+board[2]+' | '+board[3])
    print('    | '+'  | ')

#Step - 2
#Takes player input
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Do you want to be X or O? ").upper()
    player_1 = marker
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1,player_2)


#Step - 3
#Edit the place
def place_marker(board,marker,position):
    board[position] = marker

#Step - 4
#Win Check
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
     (board[4] == mark and board[5] == mark and board[6] == mark) or 
     (board[1] == mark and board[2] == mark and board[3] == mark) or 
     (board[1] == mark and board[5] == mark and board[9] == mark) or 
     (board[3] == mark and board[5] == mark and board[7] == mark) or
     (board[1] == mark and board[4] == mark and board[7] == mark) or 
     (board[2] == mark and board[5] == mark and board[8] == mark) or 
     (board[3] == mark and board[6] == mark and board[9] == mark))

#Step - 5
#Randomly decide first player
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Step - 6
#Check the space on the board
def space_check(board,positon):
    return board[positon] == ' '
    
#Step - 7
#Check if board is full 
def full_board_check(board):
    for i in range(1,len(board)):
        if space_check(board,i):
            return False
    return True

#Step - 8
#Ask for player next position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#Step - 9
#Ask to play again
def replay():
    ch = ''
    while ch != 'Y' or ch !='N':
        ch = input('Do you want to play again? Enter Yes or No: ')
        if ch == 'Y' or ch =='y':
            return True
        else:
            return False

#Game Setup
print("You successfully entered the game!")

while True:
    theBoard = [' '] * 10
    player_1,player_2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input("Do you want to start the game(Y/N) : ")
    if play_game == 'Y' or play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player_1,position)
            if win_check(theBoard,player_1):
                display_board(theBoard)
                print("Congratulations! Player 1 won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is Draw!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player_2,position)
            if win_check(theBoard,player_2):
                display_board(theBoard)
                print('Congratulations! Player 2 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is Draw!")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
