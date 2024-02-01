import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to check if a player has won
def has_won(position):
    if position >= 100:
        return True
    else:
        return False

# Function to move the player
def move_player(player, steps):
    player += steps
    if player > 100:
        player = 100
    return player

# Function to check if the player has encountered a snake or ladder
def check_snake_or_ladder(player):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    if player in snakes:
        player = snakes[player]
    elif player in ladders:
        player = ladders[player]

    return player

# Function to play the game
def play_game():
    player1 = 0
    player2 = 0

    while True:
        # Player 1's turn
        print("Player 1's turn")
        input("Press Enter to roll the dice...")
        steps = roll_dice()
        print("Player 1 rolled a", steps)
        player1 = move_player(player1, steps)
        player1 = check_snake_or_ladder(player1)
        print("Player 1 is now at position", player1)

        if has_won(player1):
            print("Player 1 has won!")
            break

        # Player 2's turn
        print("Player 2's turn")
        input("Press Enter to roll the dice...")
        steps = roll_dice()
        print("Player 2 rolled a", steps)
        player2 = move_player(player2, steps)
        player2 = check_snake_or_ladder(player2)
        print("Player 2 is now at position", player2)

        if has_won(player2):
            print("Player 2 has won!")
            break

# Start the game
play_game()