from gui import Gui
import time

def main():
    gui = Gui()         # take over the whole screen

    width = gui.get_width()     # width/height of screen
    height = gui.get_height()
    # logs output to a log file
    gui.log("The width is " + str(width))
    gui.log("The height " + str(height))
    
    row = 0
    col = 0
    direction = 1
    rdirection = 1
    while True:         # game loop
        gui.clear()     # clear the screen

        gui.draw_text("Kit", col, row, "RED", "BlUE")
        if col == width - 1:
            direction = -1
        elif col == 0:
            direction = 1
        if row == height - 1:
            rdirection = -1
        elif row == 0:
            rdirection = 1
        col += direction
        row += rdirection

        gui.draw_text("Millie", width - 10, height - 1, "YELLOW", "RED")

        gui.draw_text("David", 0, 6, "BLUE", "GREEN")
        # if row < height - 1:
        #     row += 1
        

        time.sleep(0.1)            # slow down the game


        gui.refresh()   # draw the screen

    Gui.quit()          # quit gracefully

if __name__ == "__main__":
    main()