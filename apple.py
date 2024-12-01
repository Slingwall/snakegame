"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position
from snake import Snake



def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""

    def __init__(self, gui, snake):
        position = Position(random.randrange(1, gui.get_width() - 1), random.randrange(2, gui.get_height() - 1))
        while collides(position, snake.get_snake_bits()):
            position = Position(random.randrange(1, gui.get_width() - 1), random.randrange(2, gui.get_height() - 1))
        self.position = position

    def draw(self, gui):
        gui.draw_text("+", self.position.get_x(), self.position.get_y(), "GREEN", "RED")
    
    def get_position(self):
        return self.position
