"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # current_player = player(board)

    if all(EMPTY == item for row in board for item in row):
        return X

    elif any(EMPTY == item for row in board for item in row) == True:

        count_x = sum(1 for i in range(3) for j in range(3) if board[i][j] == "X")
        count_o = sum(1 for i in range(3) for j in range(3) if board[i][j] == "O")

        if count_x == 1 and count_o == 0:
            return O
        elif count_x == count_o:
            return X  # or "player"
        elif count_o > count_x:
            return O  # or "AI"
        elif count_x > count_o:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    open_positions = {
        (i, j) for i in range(3) for j in range(3) if board[i][j] not in [X, O]
    }

    return open_positions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # creates a copy such the original board doesnt change
    nboard = copy.deepcopy(board)

    open_positions = actions(nboard)
    current_player = player(nboard)  # getting who the player is

    if action == None:
        return initial_state()
    else:
        if action in open_positions:
            try:
                if current_player == X:

                    nboard[action[0]][action[1]] = X
                    return nboard
                else:

                    nboard[action[0]][action[1]] = O
                    return nboard
            except:
                return "Something wrong"
        else:
            # action NOT in open_positions
            raise Exception("Can't overwrite a cell!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    W = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
    ]

    for x in W:
        # print("\n")
        if all(board[y[0]][y[1]] == X for y in x):
            return X

        if all(board[y[0]][y[1]] == O for y in x):
            return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O]:
        return True
    elif any(EMPTY == item for row in board for item in row) == False:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):  # from the video - BOOK page 196
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        val, action = max_value(board)
    else:
        val, action = min_value(board)
    return action


def min_value(board):

    if terminal(board):
        return utility(board), None
    # v = math.inf # positive infinity
    v = 1000

    best_action = None
    for action in actions(board):

        max_v, _ = max_value(result(board, action))
        # print("max_v in min_value",max_v)

        if max_v < v:
            v = max_v
            # print("v - min_value",v)
            best_action = action
            # print("best_action - min_value",best_action)

    return v, best_action


def max_value(board):
    if terminal(board):
        return utility(board), None

    # v = -math.inf # negative infinity
    v = -1000

    best_action = None

    for action in actions(board):
        # print("here it is #1",min_value(result(board, action)))
        min_v, _ = min_value(result(board, action))

        if min_v > v:
            v = min_v
            # print("v - max_value",v)
            best_action = action
            # print("best_action - max_value",best_action)

    return v, best_action

