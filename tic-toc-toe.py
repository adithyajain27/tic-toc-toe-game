import random

def display_board(board):
    """Prints the current board state to the console."""
    for row in range(3):
        print(" ".join(board[row]))

def enter_move(board):
    """Prompts the player for a move and updates the board accordingly."""
    while True:
        
        move = input("Enter your move (1-9): ")
        try:
            move = int(move)
            if move < 1 or move > 9:
                raise ValueError
            if board[(move - 1) // 3][(move - 1) % 3] != "-":
                raise ValueError
            break
        except ValueError:
            print("Invalid move.")
            
            
            
    #to get the location
    board[(move - 1) // 3][(move - 1) % 3] = "O"  #user entry

def make_list_of_free_fields(board):
    """Returns a list of all free fields on the board."""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign,player_name):
    """Returns True if the player using the given sign has won, False otherwise."""
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

        for col in range(3):
            if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
                return True

        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True

        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True

    return False

def draw_move(board):
    """Draws the computer's move and updates the board accordingly."""
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        return  # No free fields, it's a draw

    move = random.choice(free_fields)  #random move generation

    board[move[0]][move[1]] = "X"  #system entry
print("wel come to tic_toc_toe game\n")
player_name = input("enter the player name:\t")
board = [["-" for _ in range(3)] for _ in range(3)]

print("displaying the initial board")
display_board(board)
print("\n")

while True:
    
    print("user entry:")
    enter_move(board);print("\n")
    
    display_board(board)

    if victory_for(board, "O", player_name):
        print(f"Player {player_name} wins!")
        break
    
    if not make_list_of_free_fields(board):
        print("Draw!")
        break
    
    print("system entry:")
    draw_move(board)
    display_board(board)

    if victory_for(board, "X",player_name='system'):
        print("Computer wins!")
        break

    
    if not make_list_of_free_fields(board):
        print("Draw!")
        break
