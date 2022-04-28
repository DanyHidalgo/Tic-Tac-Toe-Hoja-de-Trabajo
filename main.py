'''
Tic-tac-toe game utils.

'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board, pos, player):
    # TODO: modificar tablero con nuevo movimiento del jugador en posicion indicada.

    if pos == 1:
        board[0][0] = player
        return board
    
    if pos == 2:
        board[0][1] = player
        return board
    
    if pos == 3:
        board[0][2] = player
        return board
    
    if pos == 4:
        board[1][0] = player
        return board

    if pos == 5:
        board[1][1] = player
        return board
    
    if pos == 6:
        board[1][2] = player
        return board
    
    if pos == 7:
        board[2][0] = player
        return board

    if pos == 8:
        board[2][1] = player
        return board
    
    if pos == 9:
        board[2][2] = player
        return board



def check_for_winner(board, player):
    # TODO: evaluar si el jugador indicado ha ganado la partida.
    pass


'''
Testing: 
'''


board = create_empty_board()
for i in range(1, len(board()):
    update_board(board, i, "X")
print_board(board)