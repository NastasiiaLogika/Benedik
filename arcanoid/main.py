import pygame
pygame.init()
back = (255, 255, 255)
window = pygame.display.set_mode((800, 600))
window.fill(back)
clock = pygame.time.Clock()
platform_x = 200
platform_y = 330
game_over = False
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = None
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename).convert_alpha()

    def draw(self):
        scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        window.blit(scaled_image, (self.rect.x, self.rect.y))


ball = Picture('ball-r.png', 160, 200, 50, 50)
platform = Picture('platform-r.png', platform_x, platform_y, 100, 30)

start_x = 5
start_y = 5
count = 9
monsters = []

for j in range(3):
    y = start_y + (55*j)
    x = start_x + (27.5*j)
    for i in range(count):
        d = Picture('enemy (1).png', x, y, 80, 40)
        monsters.append(d)
        x = x + 90
    count = count - 1 

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)

