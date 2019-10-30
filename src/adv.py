
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player("Mike", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def game_intro():
    print("\nWelcome to Mike's Adventure!\n")

    while True:
        print("\n---------------------")
        print(f"Your current location: {player.current_room}")
        print("---------------------")
        direction = input("\nWhich direction would you like to travel? ")

        def check_direction(dir):
            if dir:
                player.move(dir)
            else:
                print(
                    "\n-------\nSorry brah,you can't go that way! Try a different direction\n-------")

        if direction == "n":
            check_direction(player.current_room.n_to)
        elif direction == "w":
            check_direction(player.current_room.w_to)
        elif direction == "s":
            check_direction(player.current_room.s_to)
        elif direction == "e":
            check_direction(player.current_room.e_to)
        elif direction == "q":
            print("\nSee you next time!\n")
            quit()
        else:
            print(
                "\nThat's not a direction! Please enter a cardinal direction (n, w, e, s) or q to quit\n")


game_intro()
