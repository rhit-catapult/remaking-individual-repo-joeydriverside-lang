import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    dog_image = pygame.image.load("2dogs.JPG")
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    font_object_1 = pygame.font.SysFont("comicsansms", 28)

    fonts = pygame.font.get_fonts()
    for font in sorted(fonts):
        print(font)
    
    caption_1 = font_object_1.render("Two Dogs", True, BLACK)

    font_object_2 = pygame.font.SysFont("comicsansms", 50)
    caption_2 = font_object_2.render("funny", True, WHITE)

    # Prepare the music
    bark_sound = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        screen.blit(dog_image, (0, 0))

        # Draw the text onto the screen
        screen.blit(caption_1, (screen.get_width() / 2 - caption_1.get_width() / 2, screen.get_height() - caption_1.get_height()))
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        screen.blit(caption_2, (screen.get_width() / 2 - caption_1.get_width() / 2, 0))

        # Update the screen
        pygame.display.update()


main()
