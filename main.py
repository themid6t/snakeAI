import pygame
from snake import Food, Snake
from enum import Enum

pygame.init()
pygame.display.set_caption('Snake')

#game settings
HEIGHT = 800 
WIDTH = 800
BLOCK_SIZE = 20
SPEED = 8
FPS = 120

#rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
COLOR_SNAKE = (0, 255, 0)
COLOR_FOOD = (255, 0, 0)
BLACK = (0,0,0)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

opposite = {
    'RIGHT': 'LEFT', 
    'LEFT': 'RIGHT',
    'UP': 'DOWN',
    'DOWN': 'UP'
}
        

class Main:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.scene = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.height, self.width, BLOCK_SIZE, COLOR_SNAKE)
        self.food = Food(self.height, self.width, BLOCK_SIZE, COLOR_FOOD)

        self.ai = False
    
    def get_state(self):
        """ States: [ danger straight, danger right, danger left,
                     moving left, moving right, moving up, moving down,
                     food lef t, food right, food up, food down] 

            return States=>type:np.array
        """

        pass
    
    def check_events(self):
        action = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                action = event.key
        
        if action:
            self.snake.play_step([self.ai, action])
            

    def run(self):
        frame_count = 0
        while True:
            self.check_events()

            frame_count += 1
            self.clock.tick(FPS)
            self.scene.fill(BLACK)

            if frame_count % SPEED == 0:
                self.snake.move()
                frame_count = 0
            
    
            if self.snake.head == self.food.position:
                self.snake.length += 1
                self.food = Food(self.height, self.width, BLOCK_SIZE, COLOR_FOOD)
            
            self.food.draw(self.scene)
            self.snake.draw(self.scene)
            pygame.display.update()


if __name__ == "__main__":
    game = Main(HEIGHT, WIDTH)
    game.run()