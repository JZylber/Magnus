import pygame
import math
from tablero import Board
from logica import TurnStart
from jugador import Player

def draw_piece(screen,piece,position,size):
    x,y = position
    image = pygame.image.load(f"assets/pieces/{piece.color[0]}_{piece.name}_1x_ns.png").convert_alpha()
    image = pygame.transform.scale(image, (size, size))
    screen.blit(image, (x, y))

def draw_tile_piece(screen,screen_data,piece,position):
    TILE_SIZE = screen_data["tile_size"]
    PIECE_SIZE = screen_data["tile_size"]*3/4
    START_X_POSITION = screen_data["width"] / 2 - TILE_SIZE * 4 + (TILE_SIZE - PIECE_SIZE) / 2
    START_Y_POSITION = screen_data["height"] / 2 - TILE_SIZE * 4 + (TILE_SIZE - PIECE_SIZE) / 2
    draw_piece(screen,piece,(START_X_POSITION + position[1] * TILE_SIZE, START_Y_POSITION + position[0] * TILE_SIZE),PIECE_SIZE) 

def draw_board(screen,screen_data,board : Board) -> list[list[pygame.Rect]]:
    EVEN_TILE_COLOR = pygame.Color("#7c4c3e")
    ODD_TILE_COLOR = pygame.Color("#512a2a")
    SELECTED_EVEN_TILE_COLOR = pygame.Color("#d4b2a9")
    SELECTED_ODD_TILE_COLOR = pygame.Color("#ca9999")
    TILE_SIZE = screen_data["tile_size"]
    START_X_POSITION = screen_data["width"] / 2 - TILE_SIZE * 4
    START_Y_POSITION = screen_data["height"] / 2 - TILE_SIZE * 4
    tiles = []
    for i in range(8):
        row = []
        for j in range(8):
            selected = screen_data["selected_tile"] == (7-i,j)
            if (i + j) % 2 == 0:
                tile = pygame.draw.rect(screen, EVEN_TILE_COLOR if not selected else SELECTED_EVEN_TILE_COLOR, 
                                 [START_X_POSITION + j * TILE_SIZE, START_Y_POSITION + i * TILE_SIZE, TILE_SIZE, TILE_SIZE])
            else:
                tile = pygame.draw.rect(screen, ODD_TILE_COLOR if not selected else SELECTED_ODD_TILE_COLOR, 
                                 [START_X_POSITION + j * TILE_SIZE, START_Y_POSITION + i * TILE_SIZE, TILE_SIZE, TILE_SIZE])
            row.append(tile)
            piece = board.get_piece((7-i,j))
            if piece:
                draw_tile_piece(screen,screen_data,piece,(i,j))
        tiles.append(row)
    return tiles

def draw_player(player: Player, screen, screen_data,  left = True):
    points_font = pygame.font.SysFont("montserrat", 30)
    points = 0
    try:
        points = player.points()
    except:
        pass
    label = points_font.render(f"{player.color}: {points}", 1, (0,0,0))
    side_space = (screen_data["width"] - (screen_data["tile_size"] * 8)) / 2
    center = side_space/2 if left else screen_data["width"] - side_space/2
    screen.blit(label, (center - label.get_width() / 2, 50))
    captured_pieces = []
    try:
        captured_pieces = player.captured_pieces()
    except:
        pass
    for i in range(math.ceil(len(captured_pieces)/4)):
        for j in range(4):
            if i * 4 + j >= len(captured_pieces):
                break
            piece = captured_pieces[i * 4 + j]
            draw_piece(screen,piece,(center - screen_data["tile_size"] * 2 + j * screen_data["tile_size"], 100 + i * screen_data["tile_size"]),screen_data["tile_size"])

def clicked_tile(tiles : list[list[pygame.Rect]],position):
    for i in range(8):
        for j in range(8):
            if tiles[i][j].collidepoint(position):
                return (7-i,j)
    return None

def main(): 
    pygame.init() 
    title_font = pygame.font.SysFont("montserrat", 50)
    debug_font = pygame.font.SysFont("montserrat", 30)
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 704
    TILE_SIZE = 64
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    screen_data = {
        "width" : SCREEN_WIDTH,
        "height" : SCREEN_HEIGHT,
        "tile_size" : TILE_SIZE,
        "player_turn" : "white",
        "selected_tile" : None,
        "captured_pieces" : [],
    }
    # TITLE OF CANVAS 
    pygame_icon = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption("Ajedrez") 
    screen.fill((255, 255, 255))

    # CREATING BOARD
    board = Board()
    white_player,black_player = Player("white"),Player("black")
    exit = False
    state = TurnStart(white_player,black_player,board,screen_data)
    debug = False
    while not exit:
        # Draw turn label
        label = title_font.render(f"{screen_data['player_turn']} turn", 1, (0,0,0))
        pygame.draw.rect(screen, (255,255,255), [0, 0, screen_data["width"], 100])
        screen.blit(label, (screen_data["width"] / 2 - label.get_width() / 2, 10))
        #Debug mode button
        debug_button = pygame.draw.rect(screen, (0,0,0), [screen_data["width"] - 200, 10, 175, 30])
        debug_label = debug_font.render("Debug", 1, (255,255,255))
        screen.blit(debug_label, (screen_data["width"] - 200 + debug_button.width / 2 - debug_label.get_width() / 2, 12.5 + debug_button.height / 2 - debug_label.get_height() / 2))
        # Draw players
        draw_player(white_player,screen,screen_data)
        draw_player(black_player,screen,screen_data,False)
        # Draw board
        tiles = draw_board(screen,screen_data,board)
        #Draw current position
        if debug:
            mouse_position = pygame.mouse.get_pos()
            current_position = clicked_tile(tiles,mouse_position)
            debug_label = debug_font.render(f"Posición actual: {current_position if current_position else ''}", 1, (0,0,0))
            screen.blit(debug_label, (screen_data["width"] / 2 - debug_label.get_width() / 2, 50))
        events = pygame.event.get()
        for event in events: 
            if event.type == pygame.QUIT: 
                exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                # Clicked debug button
                if debug_button.collidepoint(position):
                    debug = not debug
                # Clicked tile
                tile = clicked_tile(tiles,position)
                if tile:
                    state = state.onClick(tile)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

