from setup import *

class AI:
    def __init__(self, player='o'):
        self.player = player

    def minmax(self, board, maximizing):
        # terminal case
        case = board.final_state()

        # player x wins
        if case == 'x':
            return 1, None
        # player o wins
        if case == 'o':
            return -1, None
        # draw
        elif board.is_full():
            return 0, None

        # x player is trying to maximizing the score
        if maximizing:
            max_eval = -100
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 'x')
                eval = self.minmax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
            return max_eval, best_move

        # o player(AI) is trying to minimizing the score
        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minmax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            return min_eval, best_move

    def eval(self, board):
        eval, move = self.minmax(board, False)
        print(f'AI chosen to mark the square in pos {move} with the eval of: {eval}')
        return move