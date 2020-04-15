import pygame
from pygame.locals import *
import sys

import config
import othello

def add_tuple(a,b):
    if len(a)!=len(b):
        return -1
    else:
        ans=[]
        for i in range(len(a)):
            ans.append(a[i]+b[i])
        return tuple(ans)

class othello_GUI:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode(config.window_large)
        pygame.display.set_caption(config.title)

        self.othello=othello.othello(config.board_height,config.board_width)
        # 色
        self.back_green=config.back_green
        self.line_color=config.line_color
        self.stones_color={'B':config.black_color,'W':config.white_color}

        self.line_thick=config.line_thick
        # ピクセル的な高さと幅(GUI)
        self.GUIboard_origin=config.GUIboard_origin
        self.GUIboard_height=config.GUIboard_height
        self.GUIboard_width=config.GUIboard_width
        # ボードのマス的な高さと幅
        self.board_height=config.board_height
        self.board_width=config.board_width

        # ピクセル的な高さと幅(GUI)
        self.origin=config.GUIboard_origin
        self.height=config.GUIboard_height
        self.width=config.GUIboard_width
        # ボードのマス的な高さと幅
        self.height_num=config.board_height
        self.width_num=config.board_width
    
    def draw_back(self):
        # ピクセル的な高さと幅(GUI)
        origin=self.GUIboard_origin
        height=self.GUIboard_height
        width=self.GUIboard_width
        # ボードのマス的な高さと幅
        height_num=self.board_height
        width_num=self.board_width

        self.screen.fill(self.back_green)
        for i in range(height_num+1):
            add=i*height//height_num
            pygame.draw.line(self.screen,self.line_color,(origin[0],origin[1]+add),(origin[0]+width,origin[1]+add),self.line_thick)
        for i in range(width_num+1):
            add=i*width//width_num
            pygame.draw.line(self.screen,self.line_color,(origin[0]+add,origin[1]),(origin[0]+add,origin[1]+height),self.line_thick)

    # color=str, position=(int,int,int), radius=int
    def draw_stone(self,color,position,radius):
        pygame.draw.circle(self.screen,self.stones_color[color],position,radius)

    def draw_stones(self):
        # ピクセル的な高さと幅(GUI)
        origin=self.GUIboard_origin
        height=self.GUIboard_height
        width=self.GUIboard_width
        # ボードのマス的な高さと幅
        height_num=self.board_height
        width_num=self.board_width

        for i in range(height_num):
            for j in range(width_num):
                # 半径は高さのみに依存(楕円にできるようにすべきか)
                radius=height/height_num/2
                if self.othello.board[i][j] in self.stones_color:
                    self.draw_stone(self.othello.board[i][j],(int(origin[0]+radius*(1+2*i)),int(origin[1]+radius*(1+2*j))),int(radius*0.9))

    
    def run(self):
        while True:
            self.draw_back()
            self.draw_stones()
            pygame.time.wait(config.fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()


def main():
    otGUI=othello_GUI()
    otGUI.run()


if __name__=='__main__':
    main()