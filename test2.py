import pygame
import sys
clock =  pygame.time.Clock()
fps = 60
pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((700, 700))
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,50))
		self.image.fill((0,255,0))
		self.rect = self.image.get_rect()
	def update(self):
		if self.rect.left > 700:
			self.rect.right = 0
player = Player()
all_sprites.add(player)
all_sprites.draw(screen)
motion = "STOP"
run = True
while run:
	clock.tick(fps)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()
		if i.type == pygame.KEYDOWN and i.key == pygame.K_LEFT:
			motion = "LEFT"
		if i.type == pygame.KEYDOWN and i.key == pygame.K_RIGHT:
			motion = "RIGHT"
		if i.type == pygame.KEYDOWN and i.key == pygame.K_UP:
			motion = "UP"
		if i.type == pygame.KEYDOWN and i.key == pygame.K_DOWN:
			motion = "DOWN"
		if i.type == pygame.KEYUP:
			if i.key in [pygame.K_DOWN,pygame.K_UP,pygame.K_RIGHT,pygame.K_LEFT]:
				motion = "STOP"
	all_sprites.update()
	screen.fill((0,0,0))
	all_sprites.draw(screen)
	pygame.display.flip()
	if motion == "LEFT":
		player.rect.x-=10
	if motion == "RIGHT":
		player.rect.x+=10
	if motion == "UP":
		player.rect.y-=10
	if motion == "DOWN":
		player.rect.y+=10
