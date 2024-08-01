from setup import *
from Board import Board
from AI import AI

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 'x'
        self.game_mode = 'ai'
        self.running = True
        self.draw_grid()

    # drawing the tic-tac-toe board
    def draw_grid(self):
        screen.fill(BG_COLOR)

        # vertical lines
        pygame.draw.line(screen, GRID_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), GRID_WIDTH)
        pygame.draw.line(screen, GRID_COLOR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), GRID_WIDTH)

        # horizontal lines
        pygame.draw.line(screen, GRID_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), GRID_WIDTH)
        pygame.draw.line(screen, GRID_COLOR, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), GRID_WIDTH)

    def draw_xo(self, row, col):
        '''
            draw X for x player
            draw O for o player
            and position them in the center of the marked square
        '''
        center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

        if self.player == 'x':
            screen.blit(x, (center_x - x.get_width() // 2, center_y - x.get_height() // 2))
        elif self.player == 'o':
            screen.blit(o, (center_x - o.get_width() // 2, center_y - o.get_height() // 2))

    def next_turn(self):
        # change turns between two players
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'

    def change_game_mode(self):
        # changing game-mode between AI and pvp using g key
        if self.game_mode == 'ai':
            self.game_mode = 'pvp'
            print("PVP mode")
        else:
            self.game_mode == 'ai'
            print("AI mode")

    def player_controller(self, row, col, player):
        # the function responsible for marking the square by a player
        # with drawing x or o on board and change the turn to the next player
        self.board.mark_square(row, col, player)
        self.draw_xo(row, col)
        self.next_turn()

    def reset(self):
        # reset the game after pressing r key
        self.__init__()

    def overlay(self):
        # display an overlay after the game finishes
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((101, 64, 83, 200))
        screen.blit(overlay, (0, 0))

    def over(self):
        # show who is the winner
        if self.board.final_state() == 'x':
            self.overlay()
            self.display_winner("X wins", TEXT_FONT, (209, 166, 126))

        elif self.board.final_state() == 'o':
            self.overlay()
            self.display_winner("O wins", TEXT_FONT, (209, 166, 126))

        elif self.board.is_full():
            self.overlay()
            self.display_winner("Draw", TEXT_FONT, (209, 166, 126))

        return self.board.final_state() != '0' or self.board.is_full()

    def display_winner(self, text, font, text_color):
        # preparing the text to show on the screen
        txt = font.render(text, True, text_color)
        txt_rect = txt.get_rect()
        txt_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(txt, txt_rect)