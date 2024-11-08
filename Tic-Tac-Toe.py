def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print_board(board)
    
    while True:
        try:
            row = int(input(f"Player {players[current_player]}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {players[current_player]}, enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue
        
        board[row][col] = players[current_player]
        print_board(board)
        
        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()
