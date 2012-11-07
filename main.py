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

    def __repr__(self):
        return (self.x, self.y)

    # TODO: Implement dot product

    # TODO: Implement cross product

class Brick:
    def __init__(self, pos, size, color=(255,255,255)):
        self.pos = Vector(pos)
        self.size = Vector(size)
        self.color = color
        #self._rect = 

class Drawer:
    
    Drawer._drawing_functions = {
        Brick: self._draw_brick
    }

    def __init__(self, surface):
        self.surface = surface

    def draw(self, object):
        Drawer._drawing_functions[object.__class__](object)

    def _draw_brick(self, brick):
        pygame.draw.rect(screen, brick.color, brick._rect)
        #self.surface.blit(ball, ballrect)

    def _draw_ball(self, ball):
        pass


class Window:
    Window.__priorities__ = []
    Window.event_functions = dict()
    Window.bg_color = (0,0,0)
    # priority -> event_type -> set of functions

    def __init__(self, size):
        Window.register_callback(pygame.QUIT, self.on_quit)
        Window.register_callback("BEFORE_DRAWING", self.on_refresh, 0)
        Window.register_callback("DONE_DRAWING", self.on_refresh, 999)
        self.display = pygame.display.set_mode(size)

    def run(self):
        while True:
            for pygame_event in pygame.event.get():
                for event_type, funcs in Window.event_functions:
                    if pygame_event.type == event:
                        for func in funcs:
                            func(pygame_event)

    def register_callback(self, event_type, func, priority = 10):
        if not priority in Window.__priorities__:
            # TODO: XXX: We need to do this via a binary search. Currently, the priority system doesn't actually work
            # Alternatively, use a priority queue?
            Window.__priorities__.append(priority)
        if not priority in Window.event_functions:
            Window.event_functions[priority] = dict()
        if not event_type in Window.event_functions[priority]
            Window.event_functions[priority][event_type] = set()
        Window.event_functions[priority][event_type].add(func)

    def deregister_callback(self, event_type, func):
        unregistered_count = 0
        for priority, callbacks in Window.event_functions:
            if not event_type in Window.event_functions:
                Window.event_functions[event_type] = set()
            else:
                if func in Window.event_functions[event_type]:
                    Window.event_functions[event_type].remove(func)
                    unregistered_count += 1
        return unregistered_count

    def clear(self):
        screen.fill(Window.bg_color)

    def on_refresh(self):
        pygame.display.flip()

    def on_quit(self):
        sys.exit()

def setup(window_size):
    pygame.init()
    window = Window(window_size)
    drawer = Drawer(window.display)
    window.run()

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