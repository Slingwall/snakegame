"BIG EXPLOSION ON THE SCREEN WOOOOOO"

import time

import random
from typing import List

from gui import Gui
from position import Position
from snake import Snake
from apple import collides

class Explosion:
    
    def __init__(self, gui, snake):
        position = snake.snake[0]
        self.position = position
        self.snake = snake

    def blow_up(self, gui):
        for i in range(30):
            gui.draw_text("+", self.position.get_x(), self.position.get_y(), "RED", "RED")
            gui.draw_text("+", self.position.get_x(), self.position.get_y(), "RED", "RED")
            gui.draw_text("+", self.position.get_x(), self.position.get_y(), "RED", "RED")
            gui.draw_text("+", self.position.get_x(), self.position.get_y(), "RED", "RED")
            gui.refresh()
        time.sleep(1)

    def draw_explosion(self, gui):
        gui.draw_text("+", 8, 10, "RED", "RED")