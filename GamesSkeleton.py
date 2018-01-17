import pygame
import random

WIDTH = 400
HEIGHT = 500
FPS = 30

#Colors
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Game loop
running = True

while running:
	# events
	for event in pygame.event.get():
		print( event.type)
		if event.type == pygame.QUIT:
			running=False

	# Update

	# Draw
	screen.fill(BLUE)


	# After Drawing every thing
	pygame.display.flip()

pygame.quit()
















