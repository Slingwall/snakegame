"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """

    def __init__(self, width, height, snake):
        self.width = round(width/2)
        self.height = round(height/2)
        self.snake = snake
        head = Position(self.width, self.height)
        snake.append(head)
        tail1 = Position(self.width - 1, self.height)
        snake.append(tail1)
        tail2 = Position(self.width - 2, self.height)
        snake.append(tail2)
        
    def draw(self, gui):
        count = 0
        for x in self.snake:
            if x == self.snake[0]:
                gui.draw_text(Snake.direction, self.snake[0].get_x(), self.snake[0].get_y(), "WHITE", "GREEN")
            else:
                gui.draw_text("+", self.snake[count].get_x(), self.snake[count].get_y(), "WHITE", "GREEN")
            count += 1

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            self.snake[x] = self.snake[x - 1]
        if Snake.direction == ">":
            self.snake[0] = Position(self.width, self.height)
            self.width += 1
        elif Snake.direction == "<":
            self.snake[0] = Position(self.width, self.height)
            self.width -= 1
        elif Snake.direction == "^":
            self.snake[0] = Position(self.width, self.height)
            self.height -= 1
        elif Snake.direction == "V":
            self.snake[0] = Position(self.width, self.height)
            self.height += 1

    direction = ">"

    def change_direction(self, direction):
        if direction == "RIGHT" and Snake.direction != "<":
            Snake.direction = ">"
        elif direction == "LEFT" and Snake.direction != ">":
            Snake.direction = "<"
        elif direction == "UP" and Snake.direction != "V":
            Snake.direction = "^"
        elif direction == "DOWN" and Snake.direction != "^":
            Snake.direction = "V"

    def get_snake_bits(self):
        return self.snake
    
    def grow(self):
        count = 3
        new_length = Position(self.width - count, self.height)
        self.snake.append(new_length)
        count += 1