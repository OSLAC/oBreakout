import sys, pygame

class Vector(x=0, y=0, vector=None):
    def __init__(x,y):
        if vector is None:
            self.x = x
            self.y = y
        else:
            self.x = vector.x
            self.y = vector.y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    # TODO: Implement dot product

    # TODO: Implement cross product

class Brick:
    def __init__(self, pos, height=50, width=100):
        self.pos = Vector(x,y)
        self.size = Vector(height, width)

class Drawer:
    
    Drawer._drawing_functions = {
        Brick: self._draw_brick
    }

    def __init__(self, surface):
        self.surface = surface

    def draw(self, object):
        Drawer._drawing_functions[object.__class__](object)

    def _draw_brick(self, brick):
        pass

    def _draw_ball(self, ball):
        pass


class Window:
    def __init__(self, width, height):
        pygame.display.set_mode(width, height)

def setup():
    pygame.init()
    

'''
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ballrect = pygame.Rect(0, 0, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
        	sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), ballrect)
    #screen.blit(ball, ballrect)
    pygame.display.flip()
'''