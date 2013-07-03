import pygame, sys, os
from pygame.locals import *
import math
from random import randint

class Space:
	"""Space is the place"""
	def __init__(self, size):
		self.size = size
		self.render_pos = [-size[0]/2, -size[1]/2]
#		self.image = pygame.transform.rotozoom(pygame.image.load(os.path.join('assets', 'space.png')), 0, 1)
		self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
		self.image = self.image.convert_alpha()
#		self.star_surface = pygame.Surface()
#		self.stars = []
#		for i in range(100): self.stars.append(1) if (randint(0,10) > 7) else self.stars.append(0)
		
	def move(self, vector):
		self.render_pos[0] = round(self.render_pos[0] - vector[0], 4)
		self.render_pos[1] = round(self.render_pos[1] + vector[1], 4)
		
	def surf(self):
		return self.image
		
	def get_pos(self):
		return self.render_pos
		
class Star:
	def __init__(self, size, pos):
		self.pos = pos
		self.size = size
		self.surface = pygame.Surface((self.size, self.size))
		self.draw()
	
	def draw(self):
		rand = randint(100, 255)
		pygame.draw.circle(self.surface, pygame.Color(rand, rand, rand), (self.size/2, self.size/2), self.size/2)
		
	def render(self, window):
		window.blit(self.surface, self.pos)