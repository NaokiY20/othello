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

        self.grid_width=config.grid_width
        
        self.grid_pos=[]
        for i in range(self.height_num):
            tmp=[]
            radius=self.grid_width/2
            for j in range(self.width_num):
                tmp.append((int(self.origin[0]+radius+radius*2*j+self.line_thick*(j+1)),
                            int(self.origin[1]+radius+radius*2*i+self.line_thick*(i+1))))
            self.grid_pos.append(tmp)
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


    def draw_stones(self):
        for i in range(self.height_num):
            for j in range(self.width_num):
                now_stone=self.othello.board[i][j]
                if now_stone in self.stones_color:
                    pygame.draw.circle(self.screen,self.stones_color[now_stone],self.grid_pos[i][j],int(self.grid_width/2*0.9))

    
    def run(self):
        while True:
            self.draw_back()
            self.draw_stones()
            # while True:
            #     pass
            pygame.time.wait(config.fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()


def main():
    otGUI=othello_GUI()
    for i in otGUI.grid_pos:
        print(i)
    print('')
    otGUI.run()
    for i in otGUI.grid_pos:
        print(i)


if __name__=='__main__':
    main()