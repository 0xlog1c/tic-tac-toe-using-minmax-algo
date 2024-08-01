from setup import *
from Game import Game

# main function
def main():
    # initialing game object
    game = Game()
    board = game.board
    ai = game.ai
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit the game
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_game_mode()

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                # row, col => giving the index of the square after int dividing by SQUARE_SIZE
                # might cause error if player clicked on the edge of the screen as 500//166 = 3 which is out of index :)
                if board.is_square_empty(row,col) and game.running:
                    game.player_controller(row, col, game.player)

                    if game.over():
                        game.running = False

        if game.game_mode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()
            row, col = ai.eval(board)
            game.player_controller(row, col, ai.player)

            if game.over():
                game.running = False

        pygame.display.update()

if __name__ == '__main__':
    main()