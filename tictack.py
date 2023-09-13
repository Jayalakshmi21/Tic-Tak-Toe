import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 10
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create the game board
board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Set the current player (X goes first)
current_player = "X"

# Initialize game over state
game_over = False
winner = None

# Draw the game board
def draw_board():
    screen.fill(BG_COLOR)
    
    # Draw horizontal lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        
    # Draw vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
    
    # Draw X's and O's
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                draw_x(row, col)
            elif board[row][col] == "O":
                draw_o(row, col)

# Draw an X at the specified position
def draw_x(row, col):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    offset = CELL_SIZE // 4
    pygame.draw.line(screen, X_COLOR, (x - offset, y - offset), (x + offset, y + offset), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (x + offset, y - offset), (x - offset, y + offset), LINE_WIDTH)

# Draw an O at the specified position
def draw_o(row, col):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 4
    pygame.draw.circle(screen, O_COLOR, (x, y), radius, LINE_WIDTH)

# Check if a player has won
def check_win(player):
    for row in range(BOARD_SIZE):
        if all(board[row][col] == player for col in range(BOARD_SIZE)):
            return True
    
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    
    return False

# Check if the game is a draw
def check_draw():
    return all(board[row][col] != " " for row in range(BOARD_SIZE) for col in range(BOARD_SIZE))

# Handleuser input and update the game state
# ...

# Handle user input and update the game state
def handle_input():
    global current_player, game_over, winner
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Convert mouse coordinates to board indices
            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE
            
            # Check if the clicked cell is empty
            if board[row][col] == " ":
                # Update the board with the current player's symbol
                board[row][col] = current_player
                
                # Check for a win or draw
                if check_win(current_player):
                    game_over = True
                    winner = current_player
                elif check_draw():
                    game_over = True
                
                # Switch the current player
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

# Game loop
while True:
    # Handle user input
    handle_input()
    
    # Draw the game board
    draw_board()
    
    # Update the display
    pygame.display.flip()
    
    # Check for game over
    if game_over:
        if winner:
            print(f"{winner} wins! Congratulations!")
        else:
            print("It's a draw!")
        
        # Wait for a few seconds before closing the game window
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
