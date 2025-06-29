# Ava Lindgren - IT 140 - Project Two

# create constants named directions for moving between rooms
directions = ['go North', 'go South', 'go East', 'go West']

# formatting of output
bold_s = '\033[1m'   # start bold formatting
bold_e = '\033[0m'   # end bold formatting
ital_s = '\x1B[3m'   # start italics formatting
ital_e = '\x1B[0m'   # end italics formatting

# define game instructions function
def game_instructions():
    # multiline code for aesthetic formatting when output is displayed
    lines = [
        '************************************** After-Hours Text Adventure Game *************************************',
        'To win the game, the player must collect 8 items',
        'while avoiding security, or it is game over.',
        'To move: go North, go South, go East, go West',
        'To add item to inventory: get \'item name\'',
        '************************************************************************************************************'
    ]
    # iterate over the lines string while getting index and value
    for i, line in enumerate(lines):
        line = line.center(108)             # center the output using a total of 108 characters
        if 'After-Hours' in line:           # replace the original line in lines to be bold
                                            # without disrupting the output format
            line = line.replace('After-Hours Text Adventure Game',
                                f'{bold_s}After-Hours Text Adventure Game{bold_e}')
        elif 'To move' in line:             # replace the original line in lines to be italicized
                                            # without disrupting the output format
            line = line.replace('go North, go South, go East, go West',
                                f'{ital_s}go North, go South, go East, go West{ital_e}')
        elif 'get \'item name\'' in line:   # italicize again without disrupting output format
            line = line.replace('get \'item name\'',
                                f"{ital_s}get 'item name'{ital_e}")
        print(line) # display the new formatting of the game instructions

    print() # display an empty line for separation

    # get input from user with Enter key to move to next function and begin game
    input('Press Enter to begin...\n'.center(108))

# define player status display
def player_status(current_room, inventory):
    print('-' * 108)                                        # output dashed line of 108 characters for separation
    print(f'You are in the {current_room}'.center(108))     # output user's current room
    print(f'Inventory: {inventory}'.center(108))            # output user's current inventory

# define main game function
def main():
    # create dictionary of rooms with corresponding directions to link with other rooms and room items
    rooms = {
        'Lobby': { 'North': 'Main Hallway', 'South': 'Office','East': 'Kitchen', 'West': 'Art Gallery' },
        'Art Gallery': { 'North': 'Library', 'East': 'Lobby', 'item': 'Key'  },
        'Library': { 'South': 'Art Gallery','East': 'Main Hallway', 'item': 'Book' },
        'Main Hallway': { 'South': 'Lobby','East': 'Bedroom', 'West': 'Library', 'item': 'Night Goggles' },
        'Bedroom': { 'East': 'Closet', 'West': 'Main Hallway' , 'item': 'Cash' },
        'Closet': { 'West': 'Bedroom' , 'item': 'Baseball Bat' },
        'Office': { 'North': 'Lobby', 'East': 'Dining Room' , 'item': 'Security' },     # security is here!
        'Kitchen': { 'South': 'Dining Room', 'West': 'Lobby' , 'item': 'Burrito' },
        'Dining Room': { 'North': 'Kitchen', 'South': 'Basement' , 'item': 'Speed Potion' },
        'Basement': { 'North': 'Dining Room' , 'item': 'Flashlight' },
    }

    current_room = 'Lobby'  # set user's initial room to 'Lobby'
    inventory = []          # set user's initial inventory to empty
    game_instructions()     # call the game_instructions() function to display the game instructions

    # begin while True loop for gameplay
    while True:
        player_status(current_room, inventory)  # call the player_status function to display the user's
                                                # current room and inventory
        # win condition
        # if the user's inventory contains all the items from the rooms, in no specific order, they win
        if sorted(inventory) == sorted(['Key', 'Book', 'Night Goggles', 'Cash', 'Baseball Bat', 'Burrito',
                                        'Speed Potion', 'Flashlight']):
            # create variable named win containing multiline string to format
            win = ('\n***********************************************************************************************'
                   '*************'
                   '\nCongrats! You collected all the items while avoiding security!\nYou Win!'
                   '\n***********************************************************************************************'
                   '*************')
            print('-' * 108) # display separation line
            for line in win.split('\n'):    # split the text in win at the new lines and center it
                print(line.center(108))     # then display the correctly formatted string
            exit()  # exit gameplay loop

        # lose condition
        if current_room == 'Office':    # if the user's current_room is office, where security is, they lose
            # create variable named lose containing multiline string to format
            lose = ('\n**********************************************************************************************'
                    '**************'
                    '\nSecurity is here!\nGame over!'
                    '\n**********************************************************************************************'
                    '**************')
            print('-' * 108) # display separation line
            for line in lose.split('\n'):   # split the text in lose at the new lines and center it
                print(line.center(108))     # then display the correctly formatted string
            exit() # exit the gameplay loop

        # item logic
        if current_room == 'Lobby':     # if user's current room is 'Lobby', display there are no items to pick up
            print('There are no items in this room'.center(108))
        elif 'item' in rooms[current_room]: # if there is an item in room, set item variable to that item
            item = rooms[current_room]['item']
            if item in inventory:       # if that item is already in inventory, display it has already been collected
                print('You have collected all items in this room'.center(108))
            elif item == 'Night Goggles' or item == 'Cash': # if item is a plural noun, user correct grammar
                print(f'You find {item}'.center(108))       # when displaying an item is in the current room
            else: # else display that there is an item in the current room
                print(f'You find a {item}'.center(108))
        else:                                                       # else display that there are no items to
            print('There is nothing to collect here'.center(108))   # collect in the user's current room

        print('-' * 108) # display separation line of 108 characters

        # get input from user for the next move and store to variable 'move'
        move = input('Enter your move:\n'.center(108))

        # handle movement
        if move in directions:              # if the move is in directions variable
            move = move.split()[1]          # split the move input to get correct direction to next room
            if move in rooms[current_room].keys():         # if the direction is a key in dictionary of rooms, set
                current_room = rooms[current_room][move]   # current_room to corresponding room of that direction
            else:
                print('-' * 108)                                # else display a separation line and that the user
                print('You cannot go this way!'.center(108))    # cannot go in the direction that was entered

        # handle item pickup
        elif move.startswith('get '):                           # if there is an item in the current room
            item = rooms.get(current_room, {}).get('item', '')  # assign variable item to the item in current room
            # assign variable requested item to the last chars of the move by stripping the first four chars
            req_item = move[4:].strip()

            # if the item and the requested item are the item in the user's current room
            if item and req_item == item:
                if item in inventory:       # if the item is already in the user's inventory
                    print('-' * 108)        # display a separation line and message that user already has this item
                    print('You already have this item!'.center(108))
                elif item not in inventory:
                    inventory.append(item)  # else the user picks up the item and is added to user's inventory
                    print('-' * 108)                                   # display separation line
                    print(f'{item} added to inventory'.center(108))    # display item is added to user's inventory
            else:
                print('-' * 108)                                 # else display separation line and
                print('Please enter a valid move!'.center(108))  # that the user must enter a valid move for items
        else:
            print('-' * 108)                                 # else display separation line and
            print('Please enter a valid move!'.center(108))  # that the user must enter a valid move

# call main function to start program
if __name__ == '__main__':
    main()