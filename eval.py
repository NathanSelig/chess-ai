import math
import chess
import chess.engine

def stacked_pawns(color, board):
    foo = board.piece_map()
    stacked_pieces = 0
    for peice in foo:
        square = peice
        name = foo.get(peice)
        peice_above = None
        # end of top most row 56
        if square < 56:
            piece_above = board.piece_at(square + 8)
            if not peice_above:
                continue
            piece_above_type = piece_above.piece_type
            # only checking ontop of square not below so no doubles
            match color:
                case 'white':
                    if name.piece_type == 1 and name.color and piece_above_type == 1 and piece_above.color:
                        print('stacked pawns are bad')
                case 'black':
                    if name.piece_type == 1 and not name.color and piece_above_type == 1 and not piece_above.color:
                        print('stacked pawns are bad')
                        stacked_pieces += 1
    print('stacked piece' , stacked_pieces)
    return stacked_pieces


def blocked_pawns(color, board):
    foo = board.piece_map()
    stacked_pieces = 0
    for peice in foo:
        square = peice
        name = foo.get(peice)
        peice_above = None
        # end of top most row 56
        if square < 56:
            piece_above = board.piece_at(square + 8)
            if not peice_above:
                continue
            piece_above_type = piece_above.piece_type
        # only checking ontop of square not below so no doubles
            match color:
                case 'white':
                    if name.piece_type == 1 and name.color and not piece_above.color:
                        print('stacked pawns are bad')
                case 'black':
                    if name.piece_type == 1 and not name.color and piece_above.color:
                        print('stacked pawns are bad')
                        stacked_pieces += 1
    print('stacked pawn', stacked_pieces)
    return stacked_pieces


def iso_pawn(color, board):
    foo = board.piece_map()
    iso_pieces = 0
    for peice in foo:
        square = peice
        name = foo.get(peice)
        # end of top most row 56
        if not name.piece_type == 1:
            return
        if square > 7:
            pieces = []
            pieces[0] = board.piece_at(square - 7)
            pieces[1] = board.piece_at(square - 9)
        if pieces:
            piece_r = pieces[0].piece_type
            piece_l = pieces[1].piece_type
        # only checking ontop of square not below so no doubles
        match color:
            case 'white':
                if name.color:
                    pass
            case 'black':
                if not name.color:
                    pass
    print('iso' , iso_pieces)
    return iso_pieces


def evalBoard(board):
    if board.is_checkmate():
        if board.turn:
            return -math.inf
        else:
            return math.inf
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    # counts peices on the board
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    wk = len(board.pieces(chess.KING, chess.WHITE))
    bk = len(board.pieces(chess.KING, chess.BLACK))
    # value of board
    material = 1 * (wp - bp) + 3 * (wn - bn) + 3 * (wb - bb) + 5 * (wr - br) + 9 * (wq - bq) + 200 * (wk - bk) - \
        0.5 * (stacked_pawns(color='white', board=board) - stacked_pawns(color='black', board=board) +
             blocked_pawns(color='white', board=board) - blocked_pawns(color='black', board=board))

    # add it together get the value of the whole board
    if board.turn:
        print(material)
        return material 
    else:
        print(-material)
        return -material

def stockfish_evaluation(board, time_limit = .01):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2.exe")
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    return result['score']

