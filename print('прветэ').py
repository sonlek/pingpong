from pygame import *
back = (255, 253, 208)
win_width = 450
win_height = 550
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < 365:
            self.rect.x += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and  self.rect.x:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x:
            self.rect.x += self.speed
player1 = Player('Tennis_racquet.svg.png', 0, 200, 5)
player2 = Player('Tennis_racquet.svg1.png', 360, 200, 4)
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()
FPS = 120
game = True
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update_left()
    player1.reset()
    player2.update_right()
    player2.reset()
    display.update()
    clock.tick(FPS)