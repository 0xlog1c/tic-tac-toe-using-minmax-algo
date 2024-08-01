import pygame
import sys
import copy

# CONSTANTS
WIDTH = 700
HEIGHT = 700
ROWS = 3
COLS = 3
SQUARE_SIZE = WIDTH//ROWS
# COLORS
BG_COLOR = (168, 96, 93)
GRID_COLOR = (101, 64, 83)
GRID_WIDTH = 10

# load and initial pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XO")
screen.fill(BG_COLOR)
TEXT_FONT = pygame.font.Font("assets/Square.ttf", 150)

# load game assets
x_asset = pygame.image.load('assets/x.png')
x = pygame.transform.scale(x_asset, (150,150))
o_asset = pygame.image.load('assets/o.png')
o = pygame.transform.scale(o_asset, (150,150))