import pygame, sys, os
from pygame.locals import *
import math
from hero import Hero
from space import Space, Star
from random import randint

pygame.init()
fpsClock = pygame.time.Clock()

# Turn on development mode
dev = True

window_size = (640, 480)

window = pygame.display.set_mode(window_size);
pygame.display.set_caption("PyGame test");
background = pygame.Color(10, 10, 10)
greenColor = pygame.Color(128, 128, 128)

basic_font = pygame.font.SysFont(None, 20)

hero = Hero(window_size)
space = Space((10000, 10000))
parallax = Space((7071, 7071))

#surface_objects = [hero, space]

#star = Star(10, (10,10))

# Make a shitload of stars
stars = []

starcount = 10000

for i in range(starcount):
	if (i < 0.8*starcount):
		stars.append(Star(randint(1, 3), (randint(0, 10000), randint(0, 10000))))
		stars[i].render(parallax.surf())
	else:
		stars.append(Star(randint(3, 5), (randint(0, 10000), randint(0, 10000))))
		#size = randint(3, 5)
		#x = randint(0, 10000)
		#y = randint(0, 10000)
		
#stars = [Star(size, x, y) in range(starcount)].render(space.surf())
		
		stars[i].render(space.surf())

while True:
	window.fill(background)
	keys = pygame.key.get_pressed()
	
	if keys[K_UP]:
		hero.throttle()
	#if keys[K_DOWN]:
		
	if keys[K_LEFT]:
		hero.turn(0)
	if keys[K_RIGHT]:
		hero.turn(1)
	if keys[K_SPACE]:
		space.render_pos = [0,0]
		parallax.render_pos = [0,0]
	if keys[K_ESCAPE]:
		pygame.event.post(Event.QUIT)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
# Loop through objects and render them
#	for object in surface_objects:
#		window.blit(object.surf(), object.render_pos)

	hero_vector = hero.get_vector()

	space.move(hero_vector)
	parallax.move([x/1.5 for x in hero_vector])
	
	window.blit(space.surf(), space.render_pos)
	window.blit(parallax.surf(), parallax.render_pos)
	window.blit(hero.render, hero.render_pos)
	
	#star.render(space.surf())
	
	if dev:
		pygame.draw.line(window, pygame.Color(255, 255, 255), (320, 240), (320+4*hero.vel[0], 240-4*hero.vel[1]))
		text = basic_font.render("Velocity: %s" % round(hero.get_speed(), 3), True, (255, 255, 255))
		text2 = basic_font.render("Pos: %s" % space.get_pos(), True, (255, 255, 255))
		text3 = basic_font.render("Speed Direction: %s" % hero.get_speed_dir(), True, (255, 255, 255))
		window.blit(text, (20, 440))
		window.blit(text2, (20, 410))
		window.blit(text3, (20, 380))
		
	pygame.display.update()
	
	fpsClock.tick(30)