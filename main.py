
# This a Basic simulation of the game Tic-Tac-Toe

import time
import random

# First ask the user if he/she wants to make the first move
while True :
    choice = input("Hey , wanna make the first move ? Y/N : ")

    if choice != 'Y' and choice != 'N' :
        print("Oops , Try Again ..\n")
    else :
        break;



# This is the Grid where the Game Takes place
grid = [['.','.','.'],['.','.','.'],['.','.','.']]


#This function is used to display the current Grid
def disp_grid() :
    for x in grid :
        for y in x :
            print(y , end = " ")
        print("\n")


# A Function to check if the Given Input is valid or not
def check(str) :
    if(len(str) < 3) :
        return False

    if str[0].isdigit() and str[2].isdigit() :
        return True
    else :
        return False


# A Function to check if the Game is Over
def check_GameOver() :

    # Check for three Consecutive O's or X's
    for i in range(0,3) :

        # Check for Rows
        if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2] :

            if grid[i][0] == 'X' :
                print("You Win !! \n")
                return True

            elif grid[i][0] == 'O':
                print("I Win !! \n")
                return True

        # Check for Columns
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i]:

            if grid[0][i] == 'X' :
                print("You Win !! \n")
                return True

            elif grid[0][i] == 'O' :
                print("I Win !! \n")
                return True


    # Check for Main Diagonal
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] :

        if grid[1][1] == 'X' :
            print("You Win !! \n")
            return True

        elif grid[1][1] == "O" :
            print("I Win !! \n")
            return True

    # Check for Other Diagonal
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] :

        if grid[1][1] == 'X' :
            print("You Win !! \n")
            return True

        elif grid[1][1] == 'O' :
            print("I Win !! \n")
            return True

    # Check if the Grid is filled
    flag = False
    for x in range(0,3) :
        for y in range(0,3) :
            if grid[x][y] == '.' :
                flag = True

    if not(flag) :
        print("Game Tied ! \n")
        return True

    return False


# Function to make a move in the Game
def make_move() :
    # Keep Trying till you are able to make a move
    while True :

        x = random.randint(0,2)
        y = random.randint(0,2)

        if grid[x][y] == '.' :
            grid[x][y] = 'O'
            break



# Now simulate the game
while True :

    # First Display the current Grid to the Player
    disp_grid()

    # Now check of the Game is Over
    if check_GameOver() :
        break

    if choice == 'Y' :
        print("Enter the Postion of the cell where you wanna make your move (x y) : ")
        str = input()

        # Check if the Position provided by the Player is valid or not
        if not(check(str)) :
            print("Oops , Try Again ..\n")
            continue

        x = (int)(str[0])
        y = (int)(str[2])

        if grid[x-1][y-1] == '.' :
            grid[x-1][y-1] = 'X'

        else :
            print("Oops , Try Again ..\n")
            continue

        choice = 'N'

    else :
        print("My Turn : \n")

        time.sleep(1)

        # Function to make a move in the Game
        make_move()

        choice = 'Y'

print("Well Played !!")