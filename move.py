from eval import stockfish_evaluation
import math
import chess
# makes the bot move with minmax
# (depth)
# for move in board.legalMoves
# eval board with move
# if eval > best val
# eval is best val
# recursive call(depth - 1)
test_board = chess.Board()

def min_max(board, depth, max_player):
    if depth == 0 or not board.is_game_over:
        return stockfish_evaluation(board)
    if max_player:
        max_eval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = min_max(board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 9999
        for move in board.legal_moves:
            eval = min_max(board, depth - 1, True)
            min_eval = min
        return min_eval
            

print(min_max(test_board , 3 , True))