import pygame
import sys

height = 200
width = 200
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption('tic tac toe')
clock = pygame.time.Clock()
running = True
black = (0,0,0)
white = (255,255,255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.line(screen, black,(width/3,0),(width/3,height))
    pygame.draw.line(screen, black,(width*2/3,0),(width*2/3,height))
    pygame.draw.line(screen, black,(0,height/3),(width,height/3))
    pygame.draw.line(screen, black,(0,height*2/3),(width,height*2/3))
    pygame.display.flip()

pygame.display.quit()
pygame.quit()
sys.exit()