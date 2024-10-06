import chess
import chess.engine

# Stockfish engine location
engine_path = "/usr/games/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def validate_fen(fen, move):
    try:
        board = chess.Board(fen)
        result = engine.analyse(board, chess.engine.Limit(time=0.1))
        best_move = result['pv'][0].uci()
        return best_move == move
    except:
        return False
