from livewires import games

class Bird(games.Sprite):
	
	JUMP_SPEED = 10
	FALL_SPEED = 0.1
	start = False
	die = False
	
	def update(self):
		if self.start == True:
			self.jump()
			self.speed_update()
			self.check_die()
			
	def jump(self):
		
