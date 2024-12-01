[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ap3XkpO5)
# Snake
<!--- The details of the final project are [here](https://docs.google.com/document/d/14JWGw0Y7FwAedhlBc1BY9acRttgXxymbR5UTHu8rGFQ/edit#heading=h.xn53ddjakib). --->

![Snake](images/snake.png)


## Introduction

For the final project, we’re going to build a famous video game that delighted gamers have been playing for many years. The game is called **Snake!** The player maneuvers a line with the arrow keys. The goal is to get the line to eat an apple, which appears at random points on the screen. The line itself grows in length. The player loses when the head of the line runs into the border around the screen, or itself.

The final project exercises skills in:



* Reading code
* Working with conditionals, lists, loops and functions
* Working with code in multiple files
* Working with objects and classes

It uses all that you’ve learned up to this point to create a real, working arcade game. Even if you don’t have the game completely working by the due date, submit what you have, so long as it compiles and runs. You’ll get credit for the parts that you managed to get working.


## What It Should Look Like

The game should draw on the screen and display as below. The walls of the room are ‘#’, the snake is ‘+’ and an arrow for the head, and the apple is red and green, and is the asterisk ‘*’.


![game](images/game.png)


This video shows the game in action: [Video](https://drive.google.com/file/d/1Wy0NitdAo4DPAT2DEVZ2OO1z3QtUBnct/view?usp=share_link). Your snake must move and grow in the same way as the example given in the video.


## Doing Graphics

Our rendition of the game will use text graphics. That is, we will draw lines and characters using the terminal window of the screen. There is a powerful text graphics library for terminals called [ncurses](https://docs.python.org/3/howto/curses.html). **But we won’t be using ncurses directly**. I’ve provided a stripped down interface for you to use in the file “gui.py”.  The Gui[^1] class boils the complex ncurses functionality down into a set of simple functions for you to call.


### Starting the Gui

To start using the Gui, make a new Gui object, and call `start()` on it.
```
	from gui import Gui

	gui = Gui()
```

This clears the screen, and the Gui library takes control of the screen.


### User Input

We can’t use input() for user input for the game. Keystrokes have to be read immediately, as the game can’t wait for the user to press the Enter key each time.  Instead, the Gui class gives you the ability to instantly read user key presses on the keyboard. 

	c = gui.get_keypress()

The value of c is the key that was pressed. For example, if the user pressed ‘`q`’, then c would be equal to "`q`". 

If the user presses the up arrow, down arrow, left arrow or right arrow, then c would be equal to one of the following values respectively:



* `"KEY_UP"`
* `"KEY_DOWN"`
* `"KEY_LEFT"`
* `"KEY_RIGHT"`

For example, this code snippet determines if the user pressed the up arrow key:


```
    c = gui.get_keypress()
    if c == "KEY_UP":
        # the user pressed up arrow
        …
```


If the user did not press any key when you called `gui.get_keypress(), `then` c `would be equal to the empty string` "".`


### Screen Dimensions

Because you can resize the terminal window, you need a way to find out how big it is. In order to get how big the screen is, you can call the following methods:
```
	screen_height = gui.get_height();
	screen_width = gui.get_width();
```


The values returned are the number of text rows for height and the number of text columns for width.


### Drawing on the Screen

The screen coordinates are defined by `(x, y)` coordinates where `(0, 0)` is the upper left hand corner of the screen, and `(screen_width - 1, screen_height - 1)` is the lower right hand corner of the screen.


![Screen](images/screen.png)


#### Drawing a Character

To draw text, call the function:

	gui.draw_text(t, x, y, foreground_color, background_color);

This draws the text `t` at the coordinates `x` and `y` with the given colors. The color arguments are strings, such as “RED”, or “YELLOW”. The valid values for colors are:



* `"WHITE"`
* `"BLACK"`
* `"RED"`
* `"ORANGE"`
* `"YELLOW"`
* `"GREEN"`
* `"BLUE"`
* `"INDIGO"`
* `"VIOLET"`

For example, to draw the character `'X'` at position `(15, 3)` and foreground color `"BLUE"` and background color `"YELLOW" `, we will call:


```
	gui.draw_text('X', 15, 3, "BLUE", "YELLOW");
```



#### Drawing a Line

To draw a line from the coordinates `(startx, starty)` to the coordinates `(endx, endy)`, with the character c and the given colors, call


```
	gui.draw_line(c, startx, starty, endx, endy, 
    		foregroundColor, backgroundColor);
```


The coordinates and color arguments are the same as in `draw_text`.


#### Double Buffering

When you draw characters or lines on the screen, they don’t appear straight away. The updates are done in an offscreen buffer. The buffer is shown only when the `Gui.refresh()` method is called.

This is done so that the complete picture is shown all at once. Otherwise you would see the system drawing parts of the picture, one at a time. Instead, we draw the characters and lines in an offscreen buffer. When the drawing of that frame is fully complete, we call `refresh()` and show it to the user all at once. 

If you think about it, game animation is just like animating a cartoon. We show full consecutive frames of data with slight differences between them. If we do it fast enough, it appears as smooth motion on the screen.


#### Sleeping

Computers run really fast, so we have a method to slow things down so that humans have a chance to react. The method `time.sleep() `takes an argument of the number of seconds to suspend execution.  When you want to take a break from executing the program, calling `time.sleep() `does the trick. You'll see it in the main program loop.


#### Debugging with Gui.log

Because the Gui class takes over the whole screen, print() doesn't work like it usually does. Debugging with print statements is more difficult now. The Gui class includes a logging statement that allows you to log output. This output is saved, and then printed out when the program ends. Using it is simply calling

	gui.log("Whatever text you want to log")


## Structure of the Main Program

The overall code flow of the game program is shown below. 


```
    gui = Gui()                  # Make a new GUI object

      continuePlaying = True
    while continuePlaying:       # Enter the main drawing loop
        c = gui.get_keyPress()   # Get user input
        if c == …:              # React to user input here
            ...                  # Use 'break' to quit out of the loop

        gui.clear()              # Clear the screen for a fresh draw
        ...                      # Draw whatever you need to draw offscreen
        gui.refresh()            # Present the new drawing all at once 

        time.sleep(0.1)          # suspend execution to slow program down
                                 # for 1/10 of a second

                                 # Game ends when you break out of loop
    gui.quit()                   # Stop and return control to terminal
```


Wrapping this code is a set of try/catch blocks. The try/catch statements are used to make sure that if an error occurs within your program, the screen is restored properly to its original state. You can read about [Python exceptions and try/catch here](https://realpython.com/python-exceptions/) (try/catch won't be on the final).


## Starter Code

I’ve given you starter code for the project. Here’s what each file does. Study the code that I gave you to get an idea of where to start.


<table>
  <tr>
   <td>File
   </td>
   <td>What it’s For
   </td>
  </tr>
  <tr>
   <td>gui.py
   </td>
   <td>This simplifies the ncurses library and gives a set of methods to get key presses, screen dimensions, and draw characters and lines on the screen. You don’t have to worry about how gui.py is written. Just use the methods described in the Gui section above.
   </td>
  </tr>
  <tr>
   <td>play.py
   </td>
   <td>This is where the main program lives. It is the basic control loop for the entire game. <strong>Study this one first and study it closely</strong>. The basic control loop creates the Gui, creates the objects within the game, and monitors for keypresses. It also draws each object within the game. You move the snake within this loop as well.
   </td>
  </tr>
  <tr>
   <td>snake.py
   </td>
   <td>This implements the Snake itself. Think of the Snake as a list of positions representing its entire length. The head is at index 0, with the tail at subsequent positions.
   </td>
  </tr>
  <tr>
   <td>apple.py
   </td>
   <td>This implements the Apple, which is the object the snake should eat.
   </td>
  </tr>
  <tr>
   <td>room.py
   </td>
   <td>This implements the Room, including the borders around the screen.
   </td>
  </tr>
  <tr>
   <td>position.py
   </td>
   <td>This class represents an <code>(x, y) </code>position on the screen. 
   </td>
  </tr>
</table>



## Running on Linux, MacOS and Windows

Download the starter code to your own computer to start.

On Linux and MacOS, the starter code with the GUI libraries will just run without anything extra required.

If you are developing directly Windows, there is one extra step you need to do before running the starter code. You need to install the "[ncurses](https://en.wikipedia.org/wiki/Ncurses)" library, as it is not built into Python on Windows by default. The steps are as follows:



1. Make sure you have Python3 installed
2. Make sure you have a network connection
3. Then open a Windows command shell and type this command to install curses:
    * <strong><code>pip3 install windows-curses</code></strong>

This will install the curses library that the GUI class uses. If this succeeds, you may now proceed to use the starter code normally on Windows. Note: this step is necessary only for those developing directly on Windows. You don't need to do this if you are using WSL.


## What You Need To Do

**Your task is to flesh out the starter code to get a complete Snake game**. 



* The tasks all build one one another, so do them in sequence. 
* You may modify any of the code in any way you want.


### Task 1 (0 points)

Your first task is to run the starter code. If you are doing this on Windows, see the section above. You need to install an extra library before starting it. To run the starter code, execute this in a terminal or command shell.


```
    python3 play.py
```


Notice that it doesn’t do very much. 



* The room is drawn with the top wall on the top edge of the screen. 
* The other 3 walls are missing. 
* There is no snake and no apple.

The game enters an infinite loop waiting for user input. 



* **Press Control-C to interrupt the game**. 
* You may press Control-C at any time to interrupt the game while you are testing and developing the game.


### Task 2 (2 points)

Your next task is to detect when the user presses a `'q'`. When the user presses a` 'q',` the game should quit gracefully.

**Hint:**



* Start by reading the `main` program in play.py.
* The program is heavily commented.
* The main loop has a section that reads a user keypress.
* Add code to that section to break out of the main loop when the user presses ‘q’.

**Remember to test your changes after each step!**


### Task 3 (2 points)

Your next task is to fully implement the Room. Modify the Room class so that the four walls of the room are drawn when `Room.draw()` is called.

**Hint:**



* You can see how the top wall of the room is drawn in the code for `Room.draw()`.
* Follow that example and draw the left, bottom and right walls of the room.


### Task 4 (2 points)

Your next task is to implement a basic Snake. The Snake’s head (denoted by >) should start out at the center of the screen, and it should initially be three characters long, like so:

	`++> `

The Snake doesn’t have to move in this step. It just has to show up on the screen when the `Snake.draw()` method is called.

**Hint:**



* The Snake object needs to know where the center of the screen is. Modify the constructor for Snake so that the center of the screen is passed to it when the Snake object is constructed. 
* In the constructor:
    * The Snake is represented as a list of positions.
    * The head’s position is at index 0.  Create a position for the head, and add it to the list.
    * The tail’s position is represented by the rest of the list. Create two other positions that represent the tail, and add it to the list
* The `Snake.draw()` method should loop over all positions.
    * Draw the head with a ‘>’, and tail section with ‘+’ using the Gui object.


### Task 5 (3 points)

The Snake’s default direction to move is to the right, since it starts as ++>. Next, you should make the snake move right one step at a time. At each step, the snake moves one step to the right. 

When you complete this step, the snake moves right one step at each iteration of the main loop, until it eventually runs off the edge of the screen on the right hand side. That’s ok for now.

**Hint:**



* Add a `move()` method to the Snake class that takes no arguments.
* Call` snake.move()` in the main loop.
* The Snake is represented as a list, with the head at index 0 of the list.
* Starting from the end of the tail, **each element of the snake steps into the place of the element before it**. That is, each element at index i should get the value at index i - 1.
* The head then moves right by **adding 1 to the x coordinate** of the head.


### Task 6 (5 points)

Make the Snake change directions when the user presses the up, down, left, or right arrow keys. 



* When the Snake goes right, the head is >. 
* When it goes down, the head is V. 
* When it goes up, the head is ^. 
* When it goes left, the head is &lt;.

**Hint:**



* Add a member variable called `direction `to the Snake class.  The variable tells the snake which direction the head should move.
* Add a `change_direction` method to the Snake class that takes a `string direction` as an argument. The argument can be either “RIGHT”, “LEFT”, “UP” or “DOWN”.
    * When the user presses an arrow key, call `change_direction `from the main loop. The `change_direction` should set the `direction` member variable to the new direction of movement.
* The head moves in the direction of motion. Edit the `Snake.move()` method so that:
    * If the `direction` is “RIGHT”, add 1 to the x-coordinate of the head
    * If the `direction` is “LEFT”, subtract 1 from the x-coordinate of the head
    * If the `direction` is “UP”, subtract 1 from the y-coordinate of the head
    * If the `direction` is “DOWN”, add 1 to the y-coordinate of the head
* Edit the `Snake.draw()` method to draw the head correctly, depending on the value of `direction`.


### Task 7 (3 points)

The Snake shouldn’t be able to double back on itself. For example, when it’s going right, the only valid direction change is up or down. Left is not valid. Add to the code in `change_direction()` to make sure that the snake can’t double back on itself.


### Task 8 (3 points)

Your next task is to implement Apple. The Apple should be red and green in color, drawn with the * (asterisk) character, and show up in a **random** position on the screen. 

**Hint:**



* Add a `Position` variable to the Apple class to hold the position of the Apple.
* Write a function that generates random numbers in the range you want. See this link for [how to generate random numbers in Python](https://docs.python.org/3/library/random.html).
* In the constructor for Apple, call the random number function to generate the x and y coordinates of the Apple. 


### Task 9 (5 points)

The Apple shouldn’t show up on top of the borders or anywhere the Snake is.

**Hint:**



* You’ll need to pass the positions of the Snake to the constructor for Apple, so that it knows where the Snake is.
* In the constructor for Apple, call the random number function to generate the x and y coordinates of the Apple. Keep generating random coordinates until the coordinate of the Apple **doesn’t collide with the wall or the snake**.


### Task 10 (4 points)

When the Snake’s head hits the Apple, two things should happen:



1. The user gains 10 points
2. The Apple should disappear and reappear at a different spot

**Hint:**



* Initialize a variable that keeps the user’s score, before the main loop of the program.
* Add to the score whenever the Snake hits an Apple.
* You’ll have to write code in the main loop to determine when the Snake’s head collides with the Apple’s position.
* Replace the old apple object with a new instance of Apple when the Snake hits an Apple.


### Task 11 (4 points)

When the Snake hits the Apple, it should also grow in length by one. Make this happen in the code.

**Hint:**



* Add a `grow()` method to Snake.
* In the `grow()` method, add to the end of the list that holds the snake’s position.
* Call `grow()` when the Snake eats an Apple. 


### Task 12 (3 points)

The Snake shouldn’t be able to hit the borders of the screen. If it does so, the player loses and the game is over. Implement border collision detection in the code.

**Hint:**



* This is implemented in the main loop 


### Task 13 (4 points)

The Snake shouldn’t be able to hit its tail. If it does so, the player loses and the game is over. Implement self collision detection in the code.

**Hint:**



* Implement this in the main loop as well.


### Congratulations -- you now have a fully working Snake game!

If you’ve got successfully to this point, you have the **full 40 points for the final project.**


### Bonus Tasks (2 points each)

From here on, you get bonus points for any of these extra tasks:



1. When the Snake collides with itself or the wall, draw an `Explosion` at the location where the collision occurred. (Hint: make a new Explosion class).
2. When the game ends, make it print out the score.
3. When the Snake eats an Apple, make the game run faster
4. Have the current running total of the score printed at the top of the screen
5. Have extra walls appear at higher levels, e.g. after the Snake has eaten a multiple of 5 apples. The Snake is not supposed to collide with these extra walls either
6. Have multiple Apples at higher levels instead of just one


## Submitting Your Code

When you have finished, submit all your .py files uploading it to the assignment repo.

If you’ve done any of the bonus tasks, send me (see-mong.tan@wwu.edu) and your TA an email telling us what you did extra, so we will know to check for that.


## Grading

The project is manually graded. No autograding on this one.

**Please remember to confirm that your submitted files were accepted correctly**. **It is incumbent upon you to confirm that you submitted everything correctly. If your submission is empty, missing files, or doesn't run -- you will get no points.**


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     “Gui” is short for graphical user interface. In our particular case, we are drawing text graphics in the terminal window.
