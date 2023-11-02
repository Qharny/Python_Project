# Main game loop
running = True
game_over = False

while running:
    screen.fill(WHITE)
    draw_lines()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // GRID_SIZE, x // GRID_SIZE

            if game_board[row][col] == ' ':
                game_board[row][col] = current_player

                if check_win(game_board, current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    # Draw symbols
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == 'X':
                draw_x(row, col)
            elif game_board[row][col] == 'O':
                draw_o(row, col)

    pygame.display.flip()

pygame.quit()
sys.exit()
