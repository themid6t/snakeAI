import random
import pygame
from enum import Enum


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class Food:
    def __init__(self, height, width, block_size, color):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.position = self.get_random_position()
        self.color = color

    def get_random_position(self):
        return (random.randint(0, (self.width-self.block_size) // self.block_size) * self.block_size,
                random.randint(0, (self.height-self.block_size) // self.block_size) * self.block_size)

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size))





class Snake:
    def __init__(self, height, width, block_size, color) -> None:
        self.length = 3
        self.height = height
        self.width = width
        self.color = color
        self.block_size = block_size
        self.positions = [(self.height // 2, self.width // 2)]
        self.direction = Direction.RIGHT
        self.head = self.positions[0]

    def draw(self, window):
        for pos in self.positions:
            pygame.draw.rect(window, self.color, pygame.Rect(pos[0], pos[1], self.block_size, self.block_size))

    def reset(self):
        self.length = 3
        self.positions = [(self.height // 2, self.width // 2)]
        self.head = self.positions[0]
        self.direction = Direction.RIGHT

    def _collision(self):
        cur_x, cur_y = self.head
        if cur_x >= self.width or cur_x < 0 or cur_y < 0 or cur_y >= self.height:
            self.reset()

        for pos in self.positions[1:]:
            if pos == self.head:
                self.reset()

    def play_step(self, action):
        if action[0]:
            pass

        else:
            if action[1] == pygame.K_UP and self.direction != Direction.DOWN:
                self.direction = Direction.UP
            elif action[1] == pygame.K_DOWN and self.direction != Direction.UP:
                self.direction = Direction.DOWN
            elif action[1] == pygame.K_LEFT and self.direction != Direction.RIGHT:
                self.direction = Direction.LEFT
            elif action[1] == pygame.K_RIGHT and self.direction != Direction.LEFT:
                self.direction = Direction.RIGHT

    def move(self):
        cur_x, cur_y = self.head

        if self.direction == Direction.RIGHT:
            cur_x += self.block_size
        elif self.direction == Direction.LEFT:
            cur_x -= self.block_size
        elif self.direction == Direction.UP:
            cur_y -= self.block_size
        elif self.direction == Direction.DOWN:
            cur_y += self.block_size
        
        new_pos = (cur_x, cur_y)

        self.positions.insert(0, new_pos)
        self.head = self.positions[0]

        if len(self.positions) > self.length:
            self.positions.pop()
        
        self._collision()
