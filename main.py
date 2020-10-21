import pygame
import random
random.seed()
pygame.font.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocks = [(self.x, self.y), (self.x + 20, self.y),
                       (self.x + 40, self.y)]
        self.dir = 'left'

    def draw(self, window):
        for block in self.blocks:
            pygame.draw.rect(window, (255, 255, 255),
                             (block[0], block[1], 19, 19))

    def move(self):
        if self.dir == 'left':
            self.x -= 20
            self.x %= WIDTH
        if self.dir == 'right':
            self.x += 20
            self.x %= WIDTH
        if self.dir == 'up':
            self.y -= 20
            self.y %= HEIGHT
        if self.dir == 'down':
            self.y += 20
            self.y %= HEIGHT

        self.blocks.insert(0, (self.x, self.y))
        self.blocks.pop()

    def eat(self):
        if self.dir == 'left':
            self.x -= 20
        if self.dir == 'right':
            self.x += 20
        if self.dir == 'up':
            self.y -= 20
        if self.dir == 'down':
            self.y += 20

        self.blocks.insert(0, (self.x, self.y))

    def collide(self):
        if (self.x, self.y) in self.blocks[1:]:
            return True
        return False


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 19, 19))


def main():
    def draw_window(window):
        pygame.draw.rect(window, (0, 0, 0), (0, 0, WIDTH, HEIGHT))

    run = True
    clock = pygame.time.Clock()
    apple_x = random.randrange(0, 29) * 20
    apple_y = random.randrange(0, 29) * 20
    snake = Snake(300, 300)
    apple = Apple(apple_x, apple_y)
    font = pygame.font.SysFont('comicsans', 40)
    while run:
        clock.tick(7)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        snake.draw(WIN)
        apple.draw(WIN)
        if snake.collide():
            run = False
            game_over_label = font.render('Game Over', 1, (255, 0, 0))
            WIN.blit(game_over_label, ((WIDTH-game_over_label.get_width()
                                        )/2, (HEIGHT-game_over_label.get_height())/2))
            pygame.display.update()
            pygame.time.delay(3000)

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake.dir != 'right':
            snake.dir = 'left'
        if keys[pygame.K_RIGHT] and snake.dir != 'left':
            snake.dir = 'right'
        if keys[pygame.K_UP] and snake.dir != 'down':
            snake.dir = 'up'
        if keys[pygame.K_DOWN] and snake.dir != 'up':
            snake.dir = 'down'

        snake.move()

        if snake.x == apple.x and snake.y == apple.y:
            snake.eat()
            del apple
            while (apple_x, apple_y) in snake.blocks:
                apple_x = random.randrange(0, 29) * 20
                apple_y = random.randrange(0, 29) * 20
            apple = Apple(apple_x, apple_y)


main()
