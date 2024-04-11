'''
this  class is responsible for storing all the information about the current state of a chess gam. it will alse be responsible
for determining the valid moves at the current state. it will also keep a move log
'''
class GameState():
    def __init__(self):
        # bảng là một list 2 chiều 8x8. Mỗi phần tử gồm 2 thành phần
        # thành phần thứ nhất đại diện cho màu của quân cờ, "b","w"
        # thành phân thứ hai đại diện cho loại quân cờ
        # "--" đại diện cho vị trí trống trên bàn cờ
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.moveFunctions = {'p':self.getPawnMoves, 'R': self.getRookMoves, 'N':self.getKnightMoves,
                              'B':self.getBishopMoves,'Q':self.getQueenMoves, 'K': self.getKingMoves}

        # đến lượt đi của bên nào
        self.whiteToMove = True

        # tạo một danh sách ghi lại lịch sử của các nước đi
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    
    """
    hoàn tác lại nước đi
    """
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove


    """
    các nước đi cần phải xem xét
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    """
    các nước đi không cần xem xét
    """
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r,c, moves)
        return moves

    def getPawnMoves(self, r,c, moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r==6 and self.board[r-2][c] == "--":
                    moves.append(Move((r,c),(r-2,c),self.board))
            if c-1>=0 and self.board[r-1][c-1][0] == 'b': # có quân của kẻ thù để bắt ở bên trái
                moves.append(Move((r,c),(r-1,c-1),self.board))
            
            if c+1 <= 7 and self.board[r-1][c+1][0] =='b': # có quân của kẻ thủ để bắt ở bên phải
                moves.append(Move((r,c),(r-1,c+1),self.board))
        else:
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c),(r+1,c),self.board))
                if r==1 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c),(r+2,c),self.board))
            if c-1>=0 and self.board[r+1][c-1][0] == 'w': # có quân của kẻ thù để bắt ở bên trái
                moves.append(Move((r,c),(r+1,c-1),self.board))
            
            if c+1 <= 7 and self.board[r+1][c+1][0] =='w': # có quân của kẻ thủ để bắt ở bên phải
                moves.append(Move((r,c),(r+1,c+1),self.board))

    def getRookMoves(self, r,c, moves):
        directions = ((-1,0), (0,-1), (1,0), (0,1)) #up, left, down, right
        enemyColor = 'b' if self.whiteToMove else 'w'
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0<= endRow < 8 and 0<= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                        break
                    else:
                        break
                else:
                    break


    def getKnightMoves(self, r,c, moves):
        directions = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2),
                        (1, -2))
        allyColor = 'w' if self.whiteToMove else 'b'
        for i in directions:
            endRow = r + i[0]
            endCol = c + i[1]
            if 0<= endRow < 8 and 0<= endCol <8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:
                    moves.append(Move((r,c), (endRow,endCol), self.board))

    def getBishopMoves(self, r, c, moves):
        directions = ((-1,-1), (-1,1),(1,1),(1,-1))
        enemyColor = 'b' if self.whiteToMove else 'w'
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow <= 7 and 0 <= endCol <= 7:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                        break
                    else:
                        break
                else:
                    break


    def getQueenMoves(self,r ,c, moves):
        self.getRookMoves(r,c,moves)
        self.getBishopMoves(r,c,moves)

    def getKingMoves(self,r,c,moves):
        directions = ((-1,-1),(1,1),(-1,1),(1,-1),(-1,0),(1,0),(0,-1),(0,1))
        allyColor = 'w' if self.whiteToMove else 'b'
        for i in range(8):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if 0<= endRow <8 and 0<= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor:
                    moves.append(Move((r,c), (endRow,endCol), self.board))

class Move():
    # map key to value
    # key: value

    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                   "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v:k for k,v in ranksToRows.items()}

    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                   "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v:k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self. moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self,r ,c):    
        return self.colsToFiles[c] + self.rowsToRanks[r]
