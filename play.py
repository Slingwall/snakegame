"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple
from apple import collides
from explosion import Explosion

def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()

        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake(gui.get_width(), gui.get_height(), [])
        apple = Apple(gui, snake)
        explosion = Explosion(gui, snake)
        apple2 = Apple(gui, snake)
        ex_wall1 = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        ex_wall2 = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        ex_wall3 = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")

        score = 0
        time_speed = 0.1

        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            # Do something with the key press
            if c == 'q':
                gui.quit()
                break  # do something if the user wants to quit
            elif c == "KEY_UP":
                snake.change_direction("UP")
            elif c == "KEY_DOWN":
                snake.change_direction("DOWN")
            elif c == "KEY_LEFT":
                snake.change_direction("LEFT")
            elif c == "KEY_RIGHT":
                snake.change_direction("RIGHT")

            # Add your code to move the snake
            # around the screen here.
            snake.move()

            # The redraw part of the game. First clear the screen
            gui.clear()

            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui)
            apple.draw(gui)
            snake.draw(gui)

            if score >= 100:
                apple2.draw(gui)

            # scoreboard
            gui.draw_text(str(score), round(gui.get_width()/2), 0, "WHITE", "BLACK")


            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here
            if collides(apple.get_position(), snake.snake):
                score += 10
                snake.grow()
                apple = Apple(gui, snake)
                time_speed -= 0.002

            if snake.snake[0].get_x() == gui.get_width() - 1 or snake.snake[0].get_x() == 0 \
                or snake.snake[0].get_y() == 1 or snake.snake[0].get_y() == gui.get_height() - 1:
                explosion = Explosion(gui, snake)
                explosion.blow_up(gui)
                print("YOU HIT THE BORDER")
                gui.quit()
                break

            if collides(snake.snake[0], snake.snake[2:]):
                explosion = Explosion(gui, snake)
                explosion.blow_up(gui)
                print("YOU HIT YOURSELF")
                gui.quit()
                break

            if score >= 100:
                if collides(apple2.get_position(), snake.snake):
                    score += 10
                    snake.grow()
                    apple2 = Apple(gui, snake)
                    time_speed -= 0.002

            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(time_speed)

    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e

    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    print("SCORE: " + str(score))
    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here


if __name__ == "__main__":
    main()
