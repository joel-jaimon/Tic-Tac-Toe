"""
Tic Tac Toe Player
"""
import copy
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
    step_count = 0
    for row in board:
        for col in row:
            if col == X or col == O:
                step_count += 1
    if step_count % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set()
    for k in range(3):
        for l in range(3):
            if board[k][l] == EMPTY:
                a.add((k, l))
    return a



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise NotImplementedError("Please Try Again")
    temp_board = copy.deepcopy(board)
    temp_board[action[0]][action[1]] = player(temp_board)
    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        if (board[1][i] == board[2][i]  == board[0][i]):
            return board[0][i]

    if (board[1][1] == board[2][2] and board[1][1] == board[0][0]):
        return board[0][0]
    elif (board[1][1] == board[2][0] and board[1][1] == board[0][2]):
        return board[0][2]
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0




def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v


def max_val(board):
    if terminal(board):
        return utility(board)
    v = -(math.inf)
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        val = -1
        move = None
        for action in actions(board):
            value = min_val(result(board, action))
            if value > val:
                val = value
                move = action
        return move

    elif player(board) == O:
        val = 1
        move = None
        for action in actions(board):
            value = max_val(result(board, action))
            if value < val:
                val = value
                move = action
        return move


