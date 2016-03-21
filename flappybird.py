from livewires import games

class Bird(games.Sprite):
	
	JUMP_SPEED = -10
	FALL_SPEED = 0.1
	start = False
	die = False
	
	def update(self):
		if self.start == True:
			self.jump()
			self.speed_update()
			self.check_die()
			
	def jump(self):
		if games.mouse.is_pressed(0):
			self.dy = self.JUMP_SPEED
	
	def speed_update(self):
		if self.dy < 0:
			self.dy += 1
		
		if self.dy >= 0:
			self.dy += self.FALL_SPEED
