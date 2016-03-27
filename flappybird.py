from livewires import games

class Bird(games.Sprite):
	
    JUMP_SPEED = -10
    FALL_SPEED = 0.1
    start = False
    last_press = False
    die = False

    def update(self):
        if self.start:
            self.jump()
            self.speed_update()
            self.check_die()
			
    def jump(self):
        if games.mouse.is_pressed(0):
            #恩这个地方貌似有点问题
           
    def speed_update(self):
        if self.dy < 0:
            self.dy += 1
		
        if self.dy >= 0:
            self.dy += self.FALL_SPEED

    def check_die(self):
        if self.overlapping_sprites:
            self.die = True

def main():
    games.init(screen_width = 384,screen_height = 448,fps = 5)
    bird_image = games.load_image("1.png")
    bird = Bird(x = 192,y = 224,image = bird_image)
    games.screen.add(bird)
    bird.start = True
    games.screen.mainloop()

main()
