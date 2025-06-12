import random
import time
import ChessEngine as CE

# Các bảng điểm
pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "p": 1}

knightScores = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]

bishopScores = [[4, 3, 2, 1, 1, 2, 3, 4],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [4, 3, 2, 1, 1, 2, 3, 4]]

queenScores = [[1, 1, 1, 3, 1, 1, 1, 1],
               [1, 2, 3, 3, 3, 1, 1, 1],
               [1, 4, 3, 3, 3, 4, 2, 1],
               [1, 2, 3, 3, 3, 2, 2, 1],
               [1, 2, 3, 3, 3, 2, 2, 1],
               [1, 4, 3, 3, 3, 4, 2, 1],
               [1, 1, 2, 3, 3, 1, 1, 1],
               [1, 1, 1, 3, 1, 1, 1, 1]]

rookScores = [[4, 3, 4, 4, 4, 4, 3, 4],
              [4, 4, 4, 4, 4, 4, 4, 4],
              [1, 1, 2, 3, 3, 2, 1, 1],
              [1, 2, 3, 4, 4, 3, 2, 1],
              [1, 2, 3, 4, 4, 3, 2, 1],
              [1, 1, 2, 3, 3, 2, 1, 1],
              [4, 4, 4, 4, 4, 4, 4, 4],
              [4, 3, 4, 4, 4, 4, 3, 4]]

whitePawnScores = [[8, 8, 8, 8, 8, 8, 8, 8],
                   [8, 8, 8, 8, 8, 8, 8, 8],
                   [5, 6, 6, 7, 7, 6, 6, 5],
                   [2, 3, 3, 5, 5, 3, 3, 2],
                   [1, 2, 3, 4, 4, 3, 2, 1],
                   [1, 1, 2, 3, 3, 2, 1, 1],
                   [1, 1, 1, 0, 0, 1, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0]]

blackPawnScores = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 0, 0, 1, 1, 1],
                   [1, 1, 2, 3, 3, 2, 1, 1],
                   [1, 2, 3, 4, 4, 3, 2, 1],
                   [2, 3, 3, 5, 5, 3, 3, 2],
                   [5, 6, 6, 7, 7, 6, 6, 5],
                   [8, 8, 8, 8, 8, 8, 8, 8],
                   [8, 8, 8, 8, 8, 8, 8, 8]]

piecePositionScores = {
    "N": knightScores,
    "Q": queenScores,
    "B": bishopScores,
    "R": rookScores,
    "bp": blackPawnScores,
    "wp": whitePawnScores
}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

# Tìm nước đi ngẫu nhiên
def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) - 1)]

# Tìm nước đi tốt nhất (có đo thời gian)
def findBestMove(gs, validMoves):
    import time
    global nextMove
    start_time = time.time()

    tempCastleRight = CE.CastleRight(gs.currentCastlingRight.wks, gs.currentCastlingRight.bks,
                                      gs.currentCastlingRight.wqs, gs.currentCastlingRight.bqs)
    nextMove = None
    validMoves = moveOrdering(gs, validMoves)
    findMoveNegaMaxAlphaBeta(gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    gs.currentCastlingRight = tempCastleRight

    end_time = time.time()
    duration = end_time - start_time
    print(f"⏱ Thời gian suy nghĩ nước đi: {duration:.4f} giây")

    return nextMove

# Tìm nước đi bằng thuật toán NegaMax có alpha-beta pruning
def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = moveOrdering(gs, gs.getValidMoves())
        score = -findMoveNegaMaxAlphaBeta(gs, nextMoves, depth - 1, -beta, -alpha, -turnMultiplier)
        gs.undoMove()

        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore

# Chấm điểm bàn cờ
def scoreBoard(gs):
    if gs.checkMate:
        return -CHECKMATE if gs.whiteToMove else CHECKMATE
    if gs.staleMate:
        return STALEMATE

    score = 0
    for r in range(8):
        for c in range(8):
            piece = gs.board[r][c]
            if piece != "--":
                piecePositionScore = 0
                if piece[1] != "K":
                    if piece[1] == 'p':
                        piecePositionScore = piecePositionScores[piece][r][c]
                    else:
                        piecePositionScore = piecePositionScores[piece[1]][r][c]
                if piece[0] == 'w':
                    score += pieceScore[piece[1]] + 0.1 * piecePositionScore
                else:
                    score -= pieceScore[piece[1]] + 0.1 * piecePositionScore
    return score

# Sắp xếp nước đi theo độ ưu tiên
def moveOrdering(gs, validMoves):
    moveScores = []
    for move in validMoves:
        gs.makeMove(move)
        score = scoreBoard(gs)
        gs.undoMove()
        if move.isCapture:
            score += pieceScore[move.pieceCaptured[1]]
        if move.isPawnPromotion:
            score += 1
        moveScores.append(score)

    sortedMoves = [move for _, move in sorted(zip(moveScores, validMoves), key=lambda pair: pair[0], reverse=True)]
    return sortedMoves

# Kiểm tra nước đi có an toàn không
def is_move_safe(gs, move):
    gs.makeMove(move)
    opponent_moves = gs.getValidMoves()
    gs.undoMove()
    for opp_move in opponent_moves:
        if opp_move.endRow == move.endRow and opp_move.endCol == move.endCol:
            return False
    return True
