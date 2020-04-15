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
        self.marker_color=config.marker_color
        
        # ボードのマス的な高さと幅
        self.height_num=config.board_height
        self.width_num=config.board_width

        self.origin=config.GUIboard_origin
        self.grid_width=config.grid_width
        
        # ボードのグラフィック的特性
        self.line_thick=config.line_thick
        radius=self.grid_width/2
        self.grid_pos=[[(int(self.origin[0]+radius*(2*j+1)+self.line_thick*(j+1)),int(self.origin[1]+radius*(2*i+1)+self.line_thick*(i+1)))
            for j in range(self.width_num)] for i in range(self.height_num)]
        self.height=self.line_thick*(self.width_num+1)+self.grid_width*self.width_num
        self.width=self.line_thick*(self.height_num+1)+self.grid_width*self.height_num
        

    def draw_back(self):
        self.screen.fill(self.back_green)
        pygame.draw.rect(self.screen,self.line_color,Rect(self.origin[0],self.origin[1],self.width,self.height))

        for i in range(self.height_num):
            for j in range(self.width_num):
                self.draw_grid(self.back_green,self.grid_pos[i][j])

    def draw_grid(self,color,center_pos):
        pygame.draw.rect(self.screen,color,Rect(center_pos[0]-self.grid_width//2,center_pos[1]-self.grid_width//2,
                                                self.grid_width,self.grid_width))
    
    def draw_marker(self):
        self.othello.add_marker()
        for i in range(self.height_num):
            for j in range(self.width_num):
                if self.othello.board[i][j]=='R':
                    self.draw_grid(self.marker_color,self.grid_pos[i][j])

    def draw_stones(self):
        for i in range(self.height_num):
            for j in range(self.width_num):
                now_stone=self.othello.board[i][j]
                if now_stone in self.stones_color:
                    pygame.draw.circle(self.screen,self.stones_color[now_stone],self.grid_pos[i][j],int(self.grid_width/2*0.9))
    
    def _is_exit(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    
    def run(self):
        while True:
            self.draw_back()
            self.draw_stones()
            self.draw_marker()
            # while True:
            #     pass
            pygame.time.wait(config.fps)
            pygame.display.update()
            self._is_exit()


def main():
    otGUI=othello_GUI()
    otGUI.run()
    for i in otGUI.grid_pos:
        print(i)


if __name__=='__main__':
    main()