from livewires import games 
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
                                   
    

    def update(self):
        if self.start:
            self.jump()
            self.speed_update()
            #self.check_die()
			
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

    UP = 1
    DOWN = 0
    can_add = 0

    images = {UP:games.load_image("up.png"),
              DOWN:games.load_image("down.png")}
    
    def __init__(self,bottom,game,image,can_add):
        
        super(Pillar, self).__init__(image = Pillar.images[image],
                                     dx = -1.5,right = 500)
        self.bottom = bottom
        self.game = game
        self.can_add = can_add
	
    def update(self):
        if self.can_add:
            self.creat_new()

    def creat_new(self):
        if self.left == 200:
            self.game.add_pillar()
            
class Game(object):
    def add_pillar(self):
        random_bottom = random.randint(50,250)
        pillar_up = Pillar(random_bottom,self,Pillar.UP,True)
        pillar_down = Pillar(random_bottom+400,self,Pillar.DOWN,False)
        games.screen.add(pillar_up)
        games.screen.add(pillar_down)
    
    def add_bird(self):
        bird = Bird()
        games.screen.add(bird)
        bird.start = True #还没加入开始菜单于是目前是直接开始    
    
def main():
    
    game = Game()
    game.add_bird()
    game.add_pillar()
    games.screen.mainloop()

main()
