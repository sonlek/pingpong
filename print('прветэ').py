from pygame import *
back = (102, 0, 0)
win_width = 450
win_height = 550
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()
FPS = 120
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)