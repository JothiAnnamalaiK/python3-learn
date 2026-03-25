from datetime import datetime

# This is a simple implementation of a tic-tac-toe game in Python. The game is played on a 3x3 grid, and two players take turns marking the spaces in the grid with their respective symbols (X and O). The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
# The game continues until there is a winner or the grid is full, resulting in a draw.
# The code includes functions to display the board, check for a win or draw, and handle player input.


def greet():
    # greet the user and explain the rules of the game
    current_hour = datetime.now().hour
    if current_hour < 12:
        print("Good morning!")
    else:
        print("Good evening!")
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.")
    print(
        "To make a move, enter a number between 1 and 9 corresponding to the grid position:"
    )


def display_board(board):
    """Displays the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


def check_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def get_player_input(board, player):
    """Gets and validates the player's input."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("This spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    # print("Welcome to Tic-Tac-Toe!")
    greet()
    display_board(board)

    while True:
        row, col = get_player_input(board, players[current_player])
        board[row][col] = players[current_player]
        display_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player  # Switch player


if __name__ == "__main__":
    tic_tac_toe()
