import pygame
import sys
import board

screen_length = 300
screen = pygame.display.set_mode((screen_length,screen_length))
pygame.display.set_caption('tic tac toe')
clock = pygame.time.Clock()
running = True
black = (0,0,0)
white = (255,255,255)
space = 2
length = (screen_length-4*space)/3
board = board.Board()

#    name       rectangle                x                  y               side_length
topleft_rect = pygame.Rect         (space,              space,              length, length)
topcenter_rect = pygame.Rect       (2*space+length,     space,              length, length)
topright_rect = pygame.Rect        (3*space+2*length,   space,              length, length)

midleft_rect = pygame.Rect         (space,              2*space+length,     length, length)
mid_rect = pygame.Rect             (2*space+length,     2*space+length,     length, length)
midright_rect = pygame.Rect        (3*space+2*length,   2*space+length,     length, length)

bottomleft_rect = pygame.Rect      (space,              3*space+2*length,   length, length)
bottomcenter_rect = pygame.Rect    (2*space+length,     3*space+2*length,   length, length)
bottomright_rect = pygame.Rect     (3*space+2*length,   3*space+2*length,   length, length)

rects = [topleft_rect,topcenter_rect,topright_rect,midleft_rect,mid_rect,midright_rect,bottomleft_rect,\
bottomcenter_rect,bottomright_rect]

list_of_box_names = []
for box_name in board.boxes.keys():
    list_of_box_names.append(box_name)   

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for rectangle in rects:
                if rectangle.collidepoint(x, y):
                    board.boxes[list_of_box_names[rects.index(rectangle)]].fill()

    screen.fill(black)

    for rect in rects:
        pygame.draw.rect(screen, white, rect)

    for box in board.boxes.values():
        print(box.isFilled)

    pygame.display.flip()

pygame.display.quit()
pygame.quit()
sys.exit()