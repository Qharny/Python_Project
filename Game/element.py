def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE), LINE_WIDTH)

def draw_x(row, col):
    offset = GRID_SIZE // 4
    pygame.draw.line(screen, LINE_COLOR, (col * GRID_SIZE + offset, row * GRID_SIZE + offset),
                     ((col + 1) * GRID_SIZE - offset, (row + 1) * GRID_SIZE - offset), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((col + 1) * GRID_SIZE - offset, row * GRID_SIZE + offset),
                     (col * GRID_SIZE + offset, (row + 1) * GRID_SIZE - offset), LINE_WIDTH)

def draw_o(row, col):
    offset = GRID_SIZE // 4
    pygame.draw.circle(screen, LINE_COLOR, (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2),
                       GRID_SIZE // 2 - offset, LINE_WIDTH)
