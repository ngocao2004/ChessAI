'''
this is our main drive file. it will be responsible for handling user input and displaying the current gamestate object
'''

import pygame as  p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #chiều của bàn cờ là 8x8
SQ_SIZE = HEIGHT//DIMENSION # kich cỡ của một ô vuông trong bàn cờ
MAX_FPS = 15 # cho animation
IMAGES = {}

'''
khởi tạo một từ điển hình ảnh toàn cục. sẽ được gọi một lần duy nhât trong main
'''

def loadImages():
    pieces = ["wp","wR","wN","wB","wQ","wK","bp","bR","bN","bB","bQ","bK"]
    for pi in pieces:
        # hàm p.transform.scale để scale lại tỉ lệ của hình ảnh sao cho khớp với ô vuông trong bàn cờ 
        IMAGES[pi] = p.transform.scale(p.image.load("images/" + pi + ".png"), (SQ_SIZE, SQ_SIZE))
    # giờ chúng ta có thể dẫn tới hình ảnh bằng cách gọi : "IMAGES['wp']"

'''
phần chính của code. đoạn này sẽ kiểm soát đầu vào của người dùng và cập nhập đồ hoạ
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    # khởi tạo một game state ban đầu
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # một biến cờ khi mà một nước đi được tạo ra

    loadImages()
    running = True
    sqSelected = () # ko có hình vuông nào được chọn, theo dõi lần click chuột cuối cùng của user ( tuple : (row, col))
    playerClicks = [] # keep track of player clicks (two tuple [(6,4), (4,4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # trả về một cặp toạ độ x y 
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): # hành động chọn 2 lần vào một ô vuông
                    # hoàn tác lại các giá trị
                    sqSelected = ()
                    playerClicks = ()
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2: # sau 2 lan click chuot
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()
                        playerClicks = []
                    else:
                        playerClicks = (sqSelected)
                    
            
            #key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # undo
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
                
        drawGameState(screen, gs)        
        clock.tick(MAX_FPS)
        p.display.flip()

"""
chịu trách nhiệm vẽ các quân cờ của trạng thái hiện tại
"""

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPiece(screen,gs.board)


"""
vẽ các hình vuông trên bàn cờ
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# vẽ các quân cờ trên bàn cờ sử dụnng GameState.board khởi đầu
def drawPiece(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()        