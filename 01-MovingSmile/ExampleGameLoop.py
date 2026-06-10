
import pygame
import sys

pygame.init()
pygame.display.set_caption("Joe Duffy")
screen = pygame.display.set_mode((700, 500))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    screen.fill(pygame.Color("Gray"))

    pygame.draw.circle(screen, pygame.Color("Yellow"), (screen.get_width() / 2, screen.get_height() / 2), 50) 

    pygame.draw.circle(screen, pygame.Color("Red"), (screen.get_width() / 2, screen.get_height() / 2), 100)

    pygame.draw.circle(screen, (255, 255, 0), (0, screen.get_height()), 10)

    pygame.display.update()
