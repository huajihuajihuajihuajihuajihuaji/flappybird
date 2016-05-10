from livewires import games 
import random

games.init(screen_width = 384,screen_height = 448,fps = 50)

class Bird(games.Animation):

    bird_images = ("1.png","2.png","3.png")
    JUMP_SPEED = -4.6
    FALL_SPEED = 0.2
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
            self.dy += self.FALL_SPEED
		
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
    
    def __init__(self,random_pos,game,image,can_add,down):
        
        super(Pillar, self).__init__(image = Pillar.images[image],
                                     dx = -1.5,right = 460)
        
        self.game = game
        self.can_add = can_add

        if down:
            self.top = random_pos
            img = self.images[0]
            rect = (0,0,70,385 - random_pos)
            n_img = img.subsurface(rect)
            self.image = n_img
            self.top =random_pos

        else:
            self.bottom = random_pos
	
    def update(self):
        if self.can_add:
            self.creat_new()

    def creat_new(self):
        if self.left == 220:
            self.game.add_pillar()

class Ground(games.Sprite):

    image = games.load_image("ground.png")
    can_add = True
    
    def __init__(self,game,x):
        super(Ground, self).__init__(image = Ground.image,
                                     dx = -1.5,x = x,y = 416)
        self.game = game
        
    def update(self):
        self.creat_new(False,0)

    def creat_new(self,correct,x):
        if self.can_add == True:
            if self.x <= 192:
                self.game.add_ground(480)
                self.can_add = False
                        
class Game(object):
    def add_pillar(self):
        random_pos = random.randint(50,200)
        pillar_up = Pillar(random_pos,self,Pillar.UP,True,False)
        pillar_down = Pillar(random_pos+120,self,Pillar.DOWN,False,True)
        games.screen.add(pillar_up)
        games.screen.add(pillar_down)
        
    
    def add_bird(self):
        bird = Bird()
        games.screen.add(bird)
        bird.start = True #还没加入开始菜单于是目前是直接开始    

    def add_ground(self,x):
        ground = Ground(self,x)
        games.screen.add(ground) 
    
def main():
    games.screen.background = games.load_image("bj.png",transparent = False)
    game = Game()
    game.add_bird()
    game.add_pillar()
    game.add_ground(192)
    games.screen.mainloop()

main()
