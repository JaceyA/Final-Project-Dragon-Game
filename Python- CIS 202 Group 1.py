"""
Final Project: Modified Dragon Realm Game
Group 1 Members: Jacey Atkinson and Leovie Lopez
CIS 202 Final Project

This is our modified version of the Dragon Realm game from Invent with Python.
Our modifications include:
- Adding a third cave (#change 1)
- Adding a player lives system (#change 2)
- Losing a life for choosing the wrong cave (#change 3)
- Removing the option to replay (#change 4)

The goal of the game is to choose the correct cave. One dragon is friendly and gives treasure,
while the other dragons are dangerous and will eat the player. The game ends when the player
runs out of lives.
"""

import random
import time

def displayIntro():
    """
    Displays the introduction text to the player.
    Explains that the player is in a land with dragons and must choose between
    three caves—one friendly and two dangerous.
    """
    print('''You are in a land full of dragons. In front of you,
you will see three caves. In one cave, the dragon is friendly
and will share his treasure with you. The others
are greedy and hungry, and will eat you on sight.
''')

#change 1: added an extra cave here
def chooseCave():
    """
    Prompts the player to choose between cave (1, 2, or 3).
    
    Returns:
        str: The chosen cave number as a string.
    """
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1, 2, or 3)')
        cave = input()
    return cave

def checkCave(chosenCave):
    """
    Simulates approaching the chosen cave and determines whether the dragon
    is friendly or deadly.

    Args:
        chosenCave (str): The cave number selected by the player.

    Returns:
        int: The number of lives lost (0 if friendly, 1 if deadly).
    """
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    #change 2: friendly cave now includes all three caves
    friendlyCave = str(random.randint(1, 3))

    if chosenCave == friendlyCave:
        print("The dragon is friendly and gives you treasure!")
        return 0  # lost 0 lives

    #change 3: added loss of life for wrong choice
    else:
        print("The dragon eats you! You lose a life.")
        return 1  # lost 1 life


player_lives = 3

while player_lives > 0:
    displayIntro()
    caveNumber = chooseCave()
    lost = checkCave(caveNumber)
    player_lives -= lost
    print(f"Lives left: {player_lives}")
    print()

#change 4: removed the option to play again, game ends when lives reach 0
print("You died.")
print("Thanks for playing!")
