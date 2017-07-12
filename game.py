from pygame.locals import *
import pygame
 
BLOCK_SIZE = 50
PLAYER_SIZE = 100
PLAYER_ACCELERATION = 1
PLAYER_STARTING_POS_X = 100
PLAYER_STARTING_POS_Y = 100
PLAYER_FRICTION = 1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
X_LIMIT = SCREEN_WIDTH - BLOCK_SIZE - PLAYER_SIZE
Y_LIMIT = SCREEN_HEIGHT - BLOCK_SIZE - PLAYER_SIZE

class Sensor:
    degree = 0
    def __init__(self, degree, range):
        self.degree = degree
        self.range = range

class Player:
    x = PLAYER_STARTING_POS_X
    y = PLAYER_STARTING_POS_Y
    dx = 0
    dy = 0
    ddx = PLAYER_ACCELERATION
    ddy = PLAYER_ACCELERATION
    sensor1 = Sensor(0, 10)
    sensor2 = Sensor(10, 10)
    sensor3 = Sensor(350, 10)
    sensors = [sensor1, sensor2, sensor3]
 
    def moveX(self):
        self.x = self.x + self.dx
 
    def moveY(self):
        self.y = self.y - self.dy
 
class Maze:
    def __init__(self):
       self.M = 20
       self.N = 15
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]
 
    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * BLOCK_SIZE , by * BLOCK_SIZE))
 
           bx = bx + 1
           if by == self.N:
               break
           if bx == self.M:
               bx = 0 
               by = by + 1
 
 
class App:
 
    windowWidth = SCREEN_WIDTH
    windowHeight = SCREEN_HEIGHT
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block.png").convert()
        self._image_surf = pygame.transform.scale(self._image_surf, (PLAYER_SIZE, PLAYER_SIZE))
        self._block_surf = pygame.transform.scale(self._block_surf, (BLOCK_SIZE, BLOCK_SIZE))
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
 
            if (keys[K_RIGHT]):
                self.player.dx += self.player.ddx
 
            elif (keys[K_LEFT]):
                self.player.dx -= self.player.ddx

            else:
                if self.player.dx < 0:
                    self.player.dx += PLAYER_FRICTION
                if self.player.dx > 0:
                    self.player.dx -= PLAYER_FRICTION
 
            if (keys[K_UP]):
                self.player.dy += self.player.ddy
 
            elif (keys[K_DOWN]):
                self.player.dy -= self.player.ddy

            else:
                if self.player.dy < 0:
                    self.player.dy += PLAYER_FRICTION
                if self.player.dy > 0:
                    self.player.dy -= PLAYER_FRICTION
 
            if (keys[K_ESCAPE]):
                self._running = False

            if self.player.x + self.player.dx < BLOCK_SIZE:
                self.player.dx = 0
                self.player.x = BLOCK_SIZE
            if self.player.x + self.player.dx > X_LIMIT:
                self.player.dx = 0
                self.player.x = X_LIMIT

            if self.player.y - self.player.dy > Y_LIMIT:
                self.player.dy = 0
                self.player.y = Y_LIMIT
            if self.player.y - self.player.dy < BLOCK_SIZE:
                self.player.dy = 0
                self.player.y = BLOCK_SIZE

            

            self.player.moveX()
            self.player.moveY()
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()