import pygame, sys, os
from pygame.locals import *
import math

class Hero:
	"""Hero"""
	# Constants
	MAX_SPEED = 0.1
	ACCEL = 0.3
	TURN_SPEED = 7
	
	def __init__(self, window_size):
		self.pos = [x/2-38 for x in window_size]
		self.render_pos = self.pos
		
		self.dir = 90
		self.vel = (0,0)
		self.surf = pygame.image.load(os.path.join('assets', 'skip.png'))
		self.rect = self.surf.get_rect()
		self.render = self.surf
	
	def turn(self, dir):
		if dir == 0:
			self.dir += self.TURN_SPEED
		elif dir == 1:
			self.dir -= self.TURN_SPEED
		
		self.dir = self.dir % 360
		self.render = pygame.transform.rotozoom(self.surf, self.dir-90, 1.0)
		
		w1, h1 = self.surf.get_size()
		w2, h2 = self.render.get_size()
		
		# Render position to keep center align
		self.render_pos = [self.pos[0]+(w1-w2)/2, self.pos[1]+(h1-h2)/2]

	def speed(self, vector):
		return math.sqrt(vector[0]**2 + vector[1]**2)
		
	def get_speed(self):
		return self.speed(self.vel)
		
	def throttle(self):
		# Add speed to given direction
		
		#if self.current_dir is not None:
		#	if math.fabs(self.current_dir - self.dir) > 90:
				#self.vel[0] = self.vel[0] + self.ACCEL*math.cos(math.radians(self.dir))
				#self.vel[1] = self.vel[1] + self.ACCEL*math.sin(math.radians(self.dir))
		#		if self.get_speed < 7: self.current_dir = None
				
		#if self.get_speed() >= 7 and self.current_dir is None:
		#	self.current_dir = self.dir
		#else:
		if self.vel < 0.2: self.vel = 0
		else:
			self.vel = (self.vel[0] + (self.ACCEL * math.cos(math.radians(self.dir))), self.vel[1] + (self.ACCEL * math.sin(math.radians(self.dir))))

	def surf(self):
		return self.render
		
	def get_vector(self):
		return self.vel
