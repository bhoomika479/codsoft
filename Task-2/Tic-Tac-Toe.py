# Tic-Tac-Toe board represented as a list of lists
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if the game is over
def is_game_over(board):
    for row in board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)) or all(board[row][col] == 'O' for row in range(3)):
            return True
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][i] == 'O' for i in range(3)):
        return True
    if all(board[i][2 - i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return True
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True
    return False

# Function to evaluate the current state of the board
def evaluate(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 10
        elif all(cell == 'O' for cell in row):
            return -10
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
            return -10
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][i] == 'O' for i in range(3)):
        return 10
    if all(board[i][2 - i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 10
    return 0

# Function to implement the Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta):
    if is_game_over(board):
        return evaluate(board)

    if is_max:
        best_val = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    val = minimax(board, depth + 1, not is_max, alpha, beta)
                    best_val = max(best_val, val)
                    alpha = max(alpha, val)
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
        return best_val
    else:
        best_val = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    val = minimax(board, depth + 1, not is_max, alpha, beta)
                    best_val = min(best_val, val)
                    beta = min(beta, val)
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
        return best_val

# Function to find the best move for the AI player
def find_best_move(board):
    best_move = (-1, -1)
    best_val = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                    alpha = max(alpha, move_val)
    return best_move

# Main game loop
while not is_game_over(board):
    display_board(board)
    player_row, player_col = map(int, input("Enter your move (row and column): ").split())
    if board[player_row][player_col] == ' ':
        board[player_row][player_col] = 'O'
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(board):
        break

    ai_row, ai_col = find_best_move(board)
    board[ai_row][ai_col] = 'X'

display_board(board)
result = evaluate(board)
if result == 10:
    print("You lose!")
elif result == -10:
    print("You win!")
else:
    print("It's a draw!")