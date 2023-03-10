import chess


def count_isolated_pawns(board):
    isolated_pawn_count = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        # If the current square is not a pawn, skip it
        if piece is None or piece.piece_type != chess.PAWN:
            continue
#need to find effeicent way to look at places where pawns are on the side 
    """ 
    o , o , o
    o , 1 , o
    o , o , o    
   what type of number means on the side like % or / by certian number need inverse for black if a
   pawn is defending 
    |  o , o
    |  P , o
    |  o , o    
    """

    return isolated_pawn_count


board = chess.Board("8/8/8/8/4P3/P2B1N2/PPPP1PPP/RNBQK2R")

isolated_pawn_count = count_isolated_pawns(board)
print(isolated_pawn_count)  # Output: 1
