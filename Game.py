""" SNAKES AND LADDERS
 By Rishiraj Tripathi
 University of Hertfordshire (20010327)
 Individual Programming Assignment """

import random
import turtle


# Introducing the Game
def intro():
    print("")
    print("**************")         # Interface for the players
    print("!!!NEW GAME!!!")         # Basic information and Important instructions
    print("**************")
    print("HOW TO PLAY- \n This is a 2 player game. Players must turn the dice chance by chance.")
    print(" Hit 'ENTER' to turn the dice.\n If you get a ladder you climb up the board.")
    print(" While, encountering a Snake will pull you down at its tail.\n First to reach EXACTLY on 25 wins the game.")
    print("NOTE-")                  # You can Win the game ONLY if land EXACTLY on 25
    print(" If the position is more than 25, the move will not be playable.\n Roll dice again till exact 25 is reached")
    print("**************")


intro()


# Asking Players to Choose their Docks
def player_name():
    print("\n Input your names and Press 'ENTER':")
    global white
    global brown


player_name()


white = input("White Cow (Player 1)=")        # Player name for White dock
brown = input("Brown Bull (Player 2)=")       # Player name for Brown dock


# Making the (5*5) Game board; Dimensions are flexible, can be changed accordingly
def grid():             # This algorithm will draw the 5*5 grid
    def box():          # This algorithm will draw the box
        turtle.hideturtle()
        turtle.speed(0)
        for i in range(4):
            turtle.forward(120)
            turtle.right(90)

    def row():          # This algorithm will draw a 5-box row
        n = 0
        while n < 5:    # No. of boxes in a row
            box()
            turtle.forward(120)
            n += 1

    turtle.title("Snakes and Ladders")      # Turtle Graphic Title
    turtle.bgcolor("light green")           # Set Background colour 'light green'
    turtle.pencolor("dark green")           # Set Pen colour 'dark green'
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-300, 300)                  # Move the cursor to specific co-ordinates to start drawing the grid
    turtle.pendown()
    r = 0
    while r < 5:        # No. of rows in a column
        row()
        turtle.penup()
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(180)
        turtle.pendown()
        r += 1


grid()


# Labeling all the boxes
def label():
    num = turtle.Turtle()       # Assigning Turtle for Numbering the Boxes
    num.hideturtle()
    num.penup()
    num.goto(200, 200)
    num.write(25, font=("Arial", 20, "normal"))
    num.goto(80, 200)
    num.write(24, font=("Arial", 20, "normal"))
    num.goto(-40, 200)
    num.write(23, font=("Arial", 20, "normal"))
    num.goto(-160, 200)
    num.write(22, font=("Arial", 20, "normal"))
    num.goto(-280, 200)
    num.write(21, font=("Arial", 20, "normal"))
    num.goto(-280, 80)
    num.write(20, font=("Arial", 20, "normal"))
    num.goto(-160, 80)
    num.write(19, font=("Arial", 20, "normal"))
    num.goto(-40, 80)
    num.write(18, font=("Arial", 20, "normal"))
    num.goto(80, 80)
    num.write(17, font=("Arial", 20, "normal"))
    num.goto(200, 80)
    num.write(16, font=("Arial", 20, "normal"))
    num.goto(200, -40)
    num.write(15, font=("Arial", 20, "normal"))
    num.goto(80, -40)
    num.write(14, font=("Arial", 20, "normal"))
    num.goto(-40, -40)
    num.write(13, font=("Arial", 20, "normal"))
    num.goto(-160, -40)
    num.write(12, font=("Arial", 20, "normal"))
    num.goto(-280, -40)
    num.write(11, font=("Arial", 20, "normal"))
    num.goto(-280, -160)
    num.write(10, font=("Arial", 20, "normal"))
    num.goto(-160, -160)
    num.write(9, font=("Arial", 20, "normal"))
    num.goto(-40, -160)
    num.write(8, font=("Arial", 20, "normal"))
    num.goto(80, -160)
    num.write(7, font=("Arial", 20, "normal"))
    num.goto(200, -160)
    num.write(6, font=("Arial", 20, "normal"))
    num.goto(200, -280)
    num.write(5, font=("Arial", 20, "normal"))
    num.goto(80, -280)
    num.write(4, font=("Arial", 20, "normal"))
    num.goto(-40, -280)
    num.write(3, font=("Arial", 20, "normal"))
    num.goto(-160, -280)
    num.write(2, font=("Arial", 20, "normal"))
    num.goto(-280, -280)
    num.write(1, font=("Arial", 20, "normal"))


label()


# Global variables for the functions below
add = turtle.addshape       # Assigning variable for adding shapes
dice = turtle.Turtle()      # Setting a turtle for Dice
snake = turtle.Turtle()     # Setting a turtle for the Snake
snake2 = turtle.Turtle()    # Setting a turtle for the Snake2
snake3 = turtle.Turtle()    # Setting a turtle for the Snake3
ladder = turtle.Turtle()    # Setting a turtle for the Ladder
ladder2 = turtle.Turtle()   # Setting a turtle for the Ladder2
ladder3 = turtle.Turtle()   # Setting a turtle for the Ladder3
bull = turtle.Turtle()      # Setting a turtle for the Bull
cow = turtle.Turtle()       # Setting a turtle for the Cow
win = turtle.Turtle()       # Setting a turtle for Win Display
win.hideturtle()

# Making all the Objects supported by Turtle

add("dice1.gif")
add("dice2.gif")
add("dice3.gif")
add("dice4.gif")
add("dice5.gif")
add("dice6.gif")
add("ladder.gif")
add("ladder2.gif")
add("ladder3.gif")
add("snake.gif")
add("snake2.gif")
add("snake3.gif")
add("bull.gif")
add("cow.gif")
add("win.gif")


# Adding required objects to the turtle
snake2.shape("snake2.gif")
snake.shape("snake.gif")
snake3.shape("snake3.gif")
ladder.shape("ladder.gif")
ladder2.shape("ladder2.gif")
ladder3.shape("ladder3.gif")
bull.shape("bull.gif")
cow.shape("cow.gif")
win.shape("win.gif")


# Function for all the shapes used
def objects():
    # Positioning the objects to specific location
    bull.penup()
    bull.goto(-310, -280)       # Move Bull to starting position

    cow.penup()
    cow.goto(-310, -200)        # Move Cow to starting position

    dice.shape("dice1.gif")
    dice.penup()
    dice.goto(-320, 0)          # Move Dice to dice position

    snake2.penup()
    snake2.goto(20, -180)       # Move Snake2 in Box 8 to 3

    snake.penup()
    snake.goto(140, 120)        # Move Snake in Box 24 to 14

    snake3.penup()
    snake3.goto(-220, -60)      # Move Snake in Box 20 to 1

    ladder.penup()
    ladder.goto(20, 180)        # Move Snake in Box 18 to 23

    ladder2.penup()
    ladder2.goto(-100, -60)     # Move Snake in Box 9 to 12

    ladder3.penup()
    ladder3.goto(260, -120)     # Move Snake in Box 5 to 15


# Function for players to be able to roll dice
def roll_dice():
    # global variables used in this function
    global white
    global brown
    global win

    # Setting the Dice Icon for 1, 2, 3, 4, 5, 6
    dice1 = turtle.Turtle()
    dice1.shape("dice1.gif")
    dice1.hideturtle()
    dice1.penup()

    dice2 = turtle.Turtle()
    dice2.shape("dice2.gif")
    dice2.hideturtle()
    dice2.penup()

    dice3 = turtle.Turtle()
    dice3.shape("dice3.gif")
    dice3.hideturtle()
    dice3.penup()

    dice4 = turtle.Turtle()
    dice4.shape("dice4.gif")
    dice4.hideturtle()
    dice4.penup()

    dice5 = turtle.Turtle()
    dice5.shape("dice5.gif")
    dice5.hideturtle()
    dice5.penup()

    dice6 = turtle.Turtle()
    dice6.shape("dice6.gif")
    dice6.hideturtle()
    dice6.penup()

    # Programming the dice and docks to move accordingly

    p_cow = 0       # Position of White Cow
    p_bull = 0      # Position of Brown Bull

    # Function for 'You Win' display
    def you_win():
        win.showturtle()
        dice.hideturtle()
        dice1.hideturtle()
        dice2.hideturtle()
        dice3.hideturtle()
        dice4.hideturtle()
        dice5.hideturtle()
        dice6.hideturtle()

    # This loop controls the movement of docks according to the dice roll
    while True:
        print("")
        input("Press 'ENTER' to roll the dice")     # Waiting for player to hit 'ENTER'
        roll = random.randint(1, 6)                 # Generate a random integer from 1 to 6 for Dice

        # Dice icons showing the respective numbers when generated
        if roll == 1:
            dice1.goto(-320, 0)     # Show generated no. at Dice position
            dice1.showturtle()
            dice2.hideturtle()
            dice3.hideturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 2:
            dice2.goto(-320, 0)     # Show generated no. at Dice position
            dice2.showturtle()
            dice3.hideturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 3:
            dice3.goto(-320, 0)     # Show generated no. at Dice position
            dice3.showturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 4:
            dice4.goto(-320, 0)     # Show generated no. at Dice position
            dice4.showturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 5:
            dice5.goto(-320, 0)     # Show generated no. at Dice position
            dice5.showturtle()
            dice6.hideturtle()

        if roll == 6:
            dice6.goto(-320, 0)     # Show generated no. at Dice position
            dice6.showturtle()

        # Loop for deciding Win
        if p_cow == 25:
            you_win()
            break

        else:
            p_cow += roll               # Increase the position no. of cow by the no. rolled

            if p_cow == 1:
                cow.goto(-220, -200)    # Animation for Moving Cow to 1

            elif p_cow == 2:
                cow.goto(-100, -200)    # Animation for Moving Cow to 2

            elif p_cow == 3:
                cow.goto(20, -200)      # Animation for Moving Cow to 3

            elif p_cow == 4:
                cow.goto(140, -200)     # Animation for Moving Cow to 4

            elif p_cow == 5:
                print("Wow!", white, ", you got a Ladder.")     # Alert player for Ladder
                p_cow += 10             # Change cow position to 15 instead of 5
                cow.goto(260, -200)
                cow.goto(260, 40)       # Animation for Moving cow to 15 from 5

            elif p_cow == 6:
                cow.goto(260, -200)
                cow.goto(260, -80)      # Animation for Moving Cow to 6

            elif p_cow == 7:
                if roll > 1:
                    cow.goto(260, -200)
                    cow.goto(260, -80)
                    cow.goto(140, -80)
                else:
                    cow.goto(140, -80)  # Animation for Moving Cow to 7

            elif p_cow == 8:
                p_cow -= 5              # Change cow position to 3 instead of 8
                print("Oops!", white, ", you stepped on a Snake")   # Alert player for Snake
                if roll > 2:
                    cow.goto(260, -200)
                    cow.goto(260, -80)
                    cow.goto(20, -80)
                    cow.goto(20, -200)
                else:
                    cow.goto(20, -80)
                    cow.goto(20, -200)  # Animation for Moving Cow to 3 from 8

            elif p_cow == 9:
                p_cow += 3              # Change cow position to 12 instead of 9
                print("Wow!", white, ", you got a Ladder.")
                if roll > 3:
                    cow.goto(260, -200)
                    cow.goto(260, -80)
                    cow.goto(-100, -80)
                    cow.goto(-100, 40)
                else:
                    cow.goto(-100, -80)
                    cow.goto(-100, 40)      # Animation for Moving Cow to 12 from 9

            elif p_cow == 10:
                if roll > 4:
                    cow.goto(260, -200)
                    cow.goto(260, -80)
                    cow.goto(-220, -80)
                else:
                    cow.goto(-220, -80)     # Animation for Moving Cow to 10

            elif p_cow == 11:
                if roll > 1:
                    cow.goto(-220, -80)
                    cow.goto(-220, 40)
                else:
                    cow.goto(-220, 40)      # Animation for Moving Cow to 11

            elif p_cow == 12:
                if roll > 2:
                    cow.goto(-220, -80)
                    cow.goto(-220, 40)
                    cow.goto(-100, 40)
                elif roll == 2:
                    cow.goto(-220, 40)
                    cow.goto(-100, 40)
                else:
                    cow.goto(-100, 40)      # Animation for Moving Cow to 12

            elif p_cow == 13:
                if roll > 3:
                    cow.goto(-220, -80)
                    cow.goto(-220, 40)
                    cow.goto(20, 40)
                elif roll == 3:
                    cow.goto(-220, 40)
                    cow.goto(20, 40)
                else:
                    cow.goto(20, 40)        # Animation for Moving Cow to 13

            elif p_cow == 14:
                if roll > 4:
                    cow.goto(-220, -80)
                    cow.goto(-220, 40)
                    cow.goto(140, 40)
                elif roll == 4:
                    cow.goto(-220, 40)
                    cow.goto(140, 40)
                else:
                    cow.goto(140, 40)       # Animation for Moving Cow to 14

            elif p_cow == 15:
                if roll > 5:
                    cow.goto(-220, -80)
                    cow.goto(-220, 40)
                    cow.goto(260, 40)
                elif roll == 5:
                    cow.goto(-220, 40)
                    cow.goto(260, 40)
                else:
                    cow.goto(260, 40)       # Animation for Moving Cow to 15

            elif p_cow == 16:
                if 6 > roll > 1:
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                elif roll == 6:
                    cow.goto(-220, -80)
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                else:
                    cow.goto(260, 160)      # Animation for Moving Cow to 16

            elif p_cow == 17:
                if roll > 2:
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                    cow.goto(140, 160)
                elif roll == 2:
                    cow.goto(260, 160)
                    cow.goto(140, 160)
                else:
                    cow.goto(140, 160)      # Animation for Moving Cow to 17

            elif p_cow == 18:
                print("Wow!", white, ", you got a Ladder.")     # Alert player for Ladder
                p_cow += 5                  # Change cow position to 23 instead of 18
                if roll > 3:
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                    cow.goto(20, 160)
                    cow.goto(20, 280)
                elif roll == 3:
                    cow.goto(260, 160)
                    cow.goto(20, 160)
                    cow.goto(20, 280)
                else:
                    cow.goto(20, 160)
                    cow.goto(20, 280)       # Animation for Moving Cow to 23 from 18

            elif p_cow == 19:
                if roll > 4:
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                    cow.goto(-100, 160)
                elif roll == 4:
                    cow.goto(260, 160)
                    cow.goto(-100, 160)
                else:
                    cow.goto(-100, 160)     # Animation for Moving Cow to 19

            elif p_cow == 20:
                print("Oops!", white, ", you stepped on a Snake")       # Alert player for Snake
                p_cow -= 19                 # Change cow position to 1 instead of 20
                if roll > 5:
                    cow.goto(260, 40)
                    cow.goto(260, 160)
                    cow.goto(-220, 160)
                    cow.goto(-220, -200)
                elif roll == 5:
                    cow.goto(260, 160)
                    cow.goto(-220, 160)
                    cow.goto(-220, -200)
                else:
                    cow.goto(-220, 160)
                    cow.goto(-220, -200)    # Animation for Moving Cow to 1 from 20

            elif p_cow == 21:
                if 6 > roll > 1:
                    cow.goto(-220, 160)
                    cow.goto(-220, 280)
                elif roll == 6:
                    cow.goto(260, 160)
                    cow.goto(-220, 160)
                    cow.goto(-220, 280)
                else:
                    cow.goto(-220, 280)     # Animation for Moving Cow to 21

            elif p_cow == 22:
                if roll > 2:
                    cow.goto(-220, 160)
                    cow.goto(-220, 280)
                    cow.goto(-100, 280)
                else:
                    cow.goto(-100, 280)     # Animation for Moving Cow to 22

            elif p_cow == 23:
                if roll > 3:
                    cow.goto(-220, 160)
                    cow.goto(-220, 280)
                    cow.goto(20, 280)
                else:
                    cow.goto(20, 280)       # Animation for Moving Cow to 23

            elif p_cow == 24:
                print("Oops!", white, ", you stepped on a Snake")   # Alert player for Snake
                p_cow -= 10                 # Change cow position to 14 instead of 24
                if roll > 4:
                    cow.goto(-220, 160)
                    cow.goto(-220, 280)
                    cow.goto(140, 280)
                    cow.goto(140, 40)
                else:
                    cow.goto(140, 280)
                    cow.goto(140, 40)       # Animation for Moving Cow to 14 from 24

        # Player interface for White Cow
        if p_cow < 25:
            print("Its a", roll, "!", white, ", you moved to", p_cow)
        elif p_cow > 25:
            p_cow -= roll           # If the player's position exceeds 25 after roll, make the move invalid
            print("Its a", roll, "!", white, ", you can't move, wait for next turn.")
        else:
            print("Its a", roll, "!", "CONGRATULATIONS!!", white, ", you Won")
            you_win()               # If the player's position is exactly 25, the player wins
            break

        print("")
        input("Press 'ENTER' to roll the dice")     # Wait for next player to hit 'ENTER'
        roll = random.randint(1, 6)                 # Generate a random no. from 1 to 6

        # Dice icons showing the respective numbers when generated
        if roll == 1:
            dice1.goto(-320, 0)
            dice1.showturtle()
            dice2.hideturtle()
            dice3.hideturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 2:
            dice2.goto(-320, 0)
            dice2.showturtle()
            dice3.hideturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 3:
            dice3.goto(-320, 0)
            dice3.showturtle()
            dice4.hideturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 4:
            dice4.goto(-320, 0)
            dice4.showturtle()
            dice5.hideturtle()
            dice6.hideturtle()

        if roll == 5:
            dice5.goto(-320, 0)
            dice5.showturtle()
            dice6.hideturtle()

        if roll == 6:
            dice6.goto(-320, 0)
            dice6.showturtle()

        # Loop for deciding Win
        if p_bull == 25:
            you_win()
            break

        else:
            p_bull += roll                  # Increase the position no. of cow by the no. rolled

            if p_bull == 1:
                bull.goto(-220, -200)       # Animation for Moving Bull to 1

            elif p_bull == 2:
                bull.goto(-100, -200)       # Animation for Moving Bull to 2

            elif p_bull == 3:
                bull.goto(20, -200)         # Animation for Moving Bull to 3

            elif p_bull == 4:
                bull.goto(140, -200)        # Animation for Moving Bull to 4

            elif p_bull == 5:
                print("Wow!", brown, ", you got a Ladder.")     # Alert player for Ladder
                p_bull += 10                # Change bull position to 15 instead of 5
                bull.goto(260, -200)
                bull.goto(260, 40)          # Animation for Moving Bull to 15 from 5

            elif p_bull == 6:
                bull.goto(260, -200)
                bull.goto(260, -80)         # Animation for Moving Bull to 6

            elif p_bull == 7:
                if roll > 1:
                    bull.goto(260, -200)
                    bull.goto(260, -80)
                    bull.goto(140, -80)
                else:
                    bull.goto(140, -80)     # Animation for Moving Bull to 7

            elif p_bull == 8:
                print("Oops!", brown, ", you stepped on a Snake")   # Alert player for Snake
                p_bull -= 5                 # Change Bull position to 3 instead of 8
                if roll > 2:
                    bull.goto(260, -200)
                    bull.goto(260, -80)
                    bull.goto(20, -80)
                    bull.goto(20, -200)
                else:
                    bull.goto(20, -80)
                    bull.goto(20, -200)     # Animation for Moving Bull to 3 from 8

            elif p_bull == 9:
                p_bull += 3                 # Change Bull position to 12 instead of 9
                print("Wow!", brown, ", you got Ladder.")   # Alert player for Ladder
                if roll > 3:
                    bull.goto(260, -200)
                    bull.goto(260, -80)
                    bull.goto(-100, -80)
                    bull.goto(-100, 40)
                else:
                    bull.goto(-100, -80)
                    bull.goto(-100, 40)     # Animation for Moving Bull to 12 from 9

            elif p_bull == 10:
                if roll > 4:
                    bull.goto(260, -200)
                    bull.goto(260, -80)
                    bull.goto(-220, -80)
                else:
                    bull.goto(-220, -80)    # Animation for Moving Bull to 10

            elif p_bull == 11:
                if roll > 1:
                    bull.goto(-220, -80)
                    bull.goto(-220, 40)
                else:
                    bull.goto(-220, 40)     # Animation for Moving Bull to 11

            elif p_bull == 12:
                if roll > 2:
                    bull.goto(-220, -80)
                    bull.goto(-220, 40)
                    bull.goto(-100, 40)
                elif roll == 2:
                    bull.goto(-220, 40)
                    bull.goto(-100, 40)
                else:
                    bull.goto(-100, 40)     # Animation for Moving Bull to 12

            elif p_bull == 13:
                if roll > 3:
                    bull.goto(-220, -80)
                    bull.goto(-220, 40)
                    bull.goto(20, 40)
                elif roll == 3:
                    bull.goto(-220, 40)
                    bull.goto(20, 40)
                else:
                    bull.goto(20, 40)       # Animation for Moving Bull to 13

            elif p_bull == 14:
                if roll > 4:
                    bull.goto(-220, -80)
                    bull.goto(-220, 40)
                    bull.goto(140, 40)
                elif roll == 4:
                    bull.goto(-220, 40)
                    bull.goto(140, 40)
                else:
                    bull.goto(140, 40)      # Animation for Moving Bull to 14

            elif p_bull == 15:
                if roll > 5:
                    bull.goto(-220, -80)
                    bull.goto(-220, 40)
                    bull.goto(260, 40)
                elif roll == 5:
                    bull.goto(-220, 40)
                    bull.goto(260, 40)
                else:
                    bull.goto(260, 40)      # Animation for Moving Bull to 15

            elif p_bull == 16:
                if 6 > roll > 1:
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                elif roll == 6:
                    bull.goto(-220, 40)
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                else:
                    bull.goto(260, 160)     # Animation for Moving Bull to 16

            elif p_bull == 17:
                if roll > 2:
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                    bull.goto(140, 160)
                elif roll == 2:
                    bull.goto(260, 160)
                    bull.goto(140, 160)
                else:
                    bull.goto(140, 160)     # Animation for Moving Bull to 17

            elif p_bull == 18:
                print("Wow!", brown, ", you got a ladder.")     # Alert player for Ladder
                p_bull += 5                 # Change Bull position to 23 instead of 18
                if roll > 3:
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                    bull.goto(20, 160)
                    bull.goto(20, 280)
                elif roll == 3:
                    bull.goto(260, 160)
                    bull.goto(20, 160)
                    bull.goto(20, 280)
                else:
                    bull.goto(20, 160)
                    bull.goto(20, 280)      # Animation for Moving Bull to 23 from 18

            elif p_bull == 19:
                if roll > 4:
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                    bull.goto(-100, 160)
                elif roll == 4:
                    bull.goto(260, 160)
                    bull.goto(-100, 160)
                else:
                    bull.goto(-100, 160)    # Animation for Moving Bull to 19

            elif p_bull == 20:
                print("Oops!", brown, ", you stepped on a Snake")   # Alert player for Snake
                p_bull -= 19                # Change Bull position to 1 instead of 20
                if roll > 5:
                    bull.goto(260, 40)
                    bull.goto(260, 160)
                    bull.goto(-220, 160)
                    bull.goto(-220, -200)
                elif roll == 5:
                    bull.goto(260, 160)
                    bull.goto(-220, 160)
                    bull.goto(-220, -200)
                else:
                    bull.goto(-220, 160)
                    bull.goto(-220, -200)   # Animation for Moving Bull to 1 from 20

            elif p_bull == 21:
                if 6 > roll > 1:
                    bull.goto(-220, 160)
                    bull.goto(-220, 280)
                elif roll == 6:
                    bull.goto(260, 40)
                    bull.goto(-220, 160)
                    bull.goto(-220, 280)
                else:
                    bull.goto(-220, 280)    # Animation for Moving Bull to 21

            elif p_bull == 22:
                if roll > 2:
                    bull.goto(-220, 160)
                    bull.goto(-220, 280)
                    bull.goto(-100, 280)
                else:
                    bull.goto(-100, 280)    # Animation for Moving Bull to 22

            elif p_bull == 23:
                if roll > 3:
                    bull.goto(-220, 160)
                    bull.goto(-220, 280)
                    bull.goto(20, 280)
                else:
                    bull.goto(20, 280)      # Animation for Moving Bull to 23

            elif p_bull == 24:
                print("Oops!", brown, ", you stepped on a Snake")   # Alert player for Snake
                p_bull -= 10                # Change Bull position to 14 instead of 24
                if roll > 4:
                    bull.goto(-220, 160)
                    bull.goto(-220, 280)
                    bull.goto(140, 280)
                    bull.goto(140, 40)
                else:
                    bull.goto(140, 280)
                    bull.goto(140, 40)      # Animation for Moving Bull to 14 from 24

        # Player interface
        if p_bull < 25:
            print("Its a", roll, "!", brown, ", you moved to", p_bull)
        elif p_bull > 25:
            p_bull -= roll          # If the player's position exceeds 25 after roll, make the move invalid
            print("Its a", roll, "!", brown, ", you can't move, wait for next turn.")
        else:
            print("Its a", roll, "!", "CONGRATULATIONS!!", brown, ", you Won")
            you_win()               # If the player's position is exactly 25, the player wins
            break


# This function will Start New Game
def new_game():
    global win
    win.hideturtle()
    intro()


# This is the Main Function for the Game
def main():
    game = True
    while game:         # While 'game' is True, the players can play the Game
        objects()
        roll_dice()
        # Ask players if they want to Exit or play New Game after every Game
        print("")
        new = input("Press 'ENTER' to Begin a New Game \n Input 'quit' to exit the game...")
        if new.lower() == "quit":
            game = False
        if game is False:
            quit()              # if players input 'quit', the Game (program) will stop
        else:
            new_game()          # if player has pressed 'ENTER' key, New Game will begin


main()
