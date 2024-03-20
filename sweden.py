import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Program")

# Define colours from https://www.pygame.org/docs/ref/color_list.html
YELLOW = pygame.Color("darkgoldenrod1")
BLUE = pygame.Color("dodgerblue2")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(BLUE)
    pygame.draw.rect(screen, YELLOW, pygame.Rect(0, 140, 600, 70))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(180, 0, 70, 600))

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
