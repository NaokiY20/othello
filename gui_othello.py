import pygame
import sys

import config
import othello

class othello_GUI:
    def __init__(self):
        self.othello=othello.othello(config.board_height,config.board_width)

        pygame.init()
        self.screen=pygame.display.set_mode(config.window_large)
        pygame.display.set_caption(config.title)
    
    def run(self):
        while True:
            pass
