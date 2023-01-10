"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    a = 0
    b = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                a += 1
            elif board[i][j] == O:
                b += 1
    if a <= b:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                s.add((i,j))
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a = action[0]
    b = action[1]
    if board[a][b] != EMPTY:
        raise Exception("Invalid move")
    board1 = [[EMPTY for i in range(len(board))]for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            board1[i][j] = board[i][j]
    h = player(board)

    board1[a][b] = h
    return board1



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == X:
        return X
    elif board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == O:
        return O

    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == X:
        return X
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == O:
        return O

    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == X:
        return X
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == O:
        return O

    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == X:
        return X
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == O:
        return O

    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == X:
        return X
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == O:
        return O

    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == X:
        return X
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == O:
        return O

    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == X:
        return X
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == O:
        return O

    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == X:
        return X
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    a = winner(board)
    if a != None:
        return True

    x = actions(board)
    if len(x) > 0:
        return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        a = winner(board)
        if a == X:
            return 1
        elif a == O:
            return -1
        else:
            return 0

def minimizing(board):
    if terminal(board):
        return utility(board)
    score = 800
    for action in actions(board):
        s = maximizing(result(board,action))
        if s < score:
            score = s
    return score
def maximizing(board):
    if terminal(board):
        return utility(board)

    score = -800
    for action in actions(board):
        s = minimizing(result(board, action))
        if s > score:
            score = s
    return score

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    key = (0, 0)
    if current_player == X:
        score = -800
        for action in actions(board):
            s = minimizing(result(board, action))
            if s > score:
                score = s
                key = action
    else:
        score = 800
        for action in actions(board):
            s = maximizing(result(board, action))
            if s < score:
                score = s
                key = action
    return key


