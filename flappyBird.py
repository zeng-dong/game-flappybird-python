import pygame
import sys


class Bird(object):
    def __init__(self):
        self.statuses = [
            pygame.image.load("./img/bird0_0.png"),
            pygame.image.load("./img/bird0_1.png"),
            pygame.image.load("./img/bird0_2.png"),
            pygame.image.load("./img/dead.png")
        ]
        self.status = 0
        self.x = 50
        self.y = 250
        self.jump = False
        self.jumpHeight = 10
        self.downHeight = 1
        self.dead = False

    def move(self):
        if self.jump:
            self.jumpHeight = self.jumpHeight - 1
            # self.y = self.y - self.jumpHeight
            self.y -= self.jumpHeight
        else:
            self.downHeight += 0.1
            self.y += self.downHeight


class Pipe(object):
    def __init__(self):
        self.wallx = 120
        self.upperHalf = pygame.image.load("./img/pipe_down.png")
        self.lowerHalf = pygame.image.load("./img/pipe_up.png")

    def move(self):
        self.wallx -= 2
        if self.wallx < -42:
            global score
            score += 10
            self.wallx = 300


def createMap():
    screen.blit(background, (0, 0))

    screen.blit(Pipe.upperHalf, (int(Pipe.wallx), -200))
    screen.blit(Pipe.lowerHalf, (int(Pipe.wallx), 362))
    Pipe.move()

    if Bird.dead:
        Bird.status = 3
    elif Bird.jump:
        Bird.status = 0
    else:
        Bird.status = 2
    screen.blit(Bird.statuses[Bird.status], (int(Bird.x), int(Bird.y)))
    Bird.move()
    font.render('Score:' + str(score), 1, (255,255,255))
    screen.blit(font.render('Score:' + str(score), 1, (255,255,255)), (90, 20) )
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)

    size = (288, 512)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    Bird = Bird()
    Pipe = Pipe()
    score = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Bird.jump = True
                    Bird.jumpHeight = 10
                    Bird.downHeight = 1

        background = pygame.image.load("./img/bg_day.png")
        createMap()

    pygame.quit()
