import pygame
pygame.init()
screenWidth = 700
screenHeight = 700
windown = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Eight Queen!!!")
white = (255, 255, 255)
black = (0, 0, 0)
squareBoard = screenWidth // 8
def chessboard():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(windown, color, (col * squareBoard, row * squareBoard, squareBoard, squareBoard))
def queen():
    position = [(0,5),(1,1),(2,6),(3,0),(4,3),(5,7),(6,4),(7,2)]
    for (i,j) in position:
        pygame.draw.rect(windown, (155,255,155,0.5), (i * squareBoard+10, j * squareBoard+10, squareBoard-20, squareBoard-20))
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    chessboard()
    queen()
    pygame.display.flip()
pygame.quit()