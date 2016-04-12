import random

games.init(screen_width = 384,screen_height = 448,fps = 50)

class Bird(games.Animation):

    bird_images = ("1.png","2.png","3.png")
    JUMP_SPEED = -13.5
    FALL_SPEED = 0.1
    start = False
    last_press = False
    die = False

    def __init__(self):
        super(Bird, self).__init__(images = Bird.bird_images,
                                   x = 192, y = 190,
                                   repeat_interval = 10, n_repeats = -1)
                                   
    def add_bird():
    	bird = Bird()
    	games.screen.add(bird)
    	bird.start = True #还没加入开始菜单于是目前是直接开始

    def update(self):
        if self.start:
            self.jump()
            self.speed_update()
            self.check_die()
			
    def jump(self):
        if games.mouse.is_pressed(0):
            if self.last_press == False:
                self.dy = self.JUMP_SPEED
                self.last_press = True

        else:
            self.last_press = False
        
            
    def speed_update(self):
        if self.dy < 0:
            self.dy += 1.5
		
        if self.dy >= 0:
            self.dy += self.FALL_SPEED

    def check_die(self):
        if self.overlapping_sprites:
            self.die = True
            self.destroy()


class Pillar(games.Sprite):
    pillar_image = games.load_image("up.png")

    def __init__(self,bottom):
        
        super(Pillar, self).__init__(image = Pillar.pillar_image,dx = -1,
                                     right = 384)
        self.bottom = bottom
	
        def creat_new():
            if self.left == 284:
                add_pillar()
		
        def add_pillar():
            random_bottom = random.randint(30,250)
            pillar = Pillar(random_bottom)
            games.screen.add(pillar)
    
def main():
    
    add_bird()
    add_pillar()
    games.screen.mainloop()

main()

