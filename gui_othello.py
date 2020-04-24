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

class cursor:
    def __init__(self):
        self.position=[0,0]

    def input_key(self,vec):
        self.position[0]+=vec[0]
        self.position[1]+=vec[1]
        if self.position[0]<0:
            self.position[0]=0
        if self.position[0]>=8:
            self.position[0]=7
        if self.position[1]<0:
            self.position[1]=0
        if self.position[1]>=8:
            self.position[1]=7


class draw_status:
    def __init__(self):
        self.status={'marker':False,'cursor':False}
        
    def init(self):
        for key in self.status.keys():
            self.status[key]=False
    
class othello_GUI:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode(config.window_large)
        pygame.display.set_caption(config.title)

        self.othello=othello.othello(config.height_num,config.width_num)
        # 色
        self.back_green=config.back_green
        self.line_color=config.line_color
        self.stones_color={'B':config.black_color,'W':config.white_color}
        self.marker_color=config.marker_color
        self.cursor_color=config.cursor_color
        
        # ボードのマス的な高さと幅
        self.height_num=config.height_num
        self.width_num=config.width_num

        # ボードのグラフィック的特性
        self.origin=config.GUIboard_origin
        self.grid_width=config.grid_width
        self.line_thick=config.line_thick
        radius=self.grid_width/2
        self.grid_pos=[[(int(self.origin[0]+radius*(2*j+1)+self.line_thick*(j+1)),int(self.origin[1]+radius*(2*i+1)+self.line_thick*(i+1)))
            for j in range(self.width_num)] for i in range(self.height_num)]
        self.board_height=self.line_thick*(self.width_num+1)+self.grid_width*self.width_num
        self.board_width=self.line_thick*(self.height_num+1)+self.grid_width*self.height_num

        self.draw_status=draw_status()
        self.cursor=cursor()    
        pygame.key.set_repeat(config.cursor_delay,config.cursor_interval)

    def draw_back(self):
        self.screen.fill(self.back_green)
        pygame.draw.rect(self.screen,self.line_color,Rect(self.origin[0],self.origin[1],self.board_width,self.board_height))

        for i in range(self.height_num):
            for j in range(self.width_num):
                self.draw_grid(self.back_green,self.grid_pos[i][j])

    def draw_grid(self,color,center_pos):
        pygame.draw.rect(self.screen,color,Rect(center_pos[0]-self.grid_width//2,center_pos[1]-self.grid_width//2,
                                                self.grid_width,self.grid_width))
    
    def draw_marker(self):
        # self.othello.add_marker()
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
    
    def draw_cursor(self):
        self.draw_grid(self.cursor_color,self.grid_pos[self.cursor.position[0]][self.cursor.position[1]])
    
    def draw_turn(self):
        turn_font=pygame.font.SysFont(None,100)
        message=turn_font.render('Turn',True,(0,0,0))
        self.screen.blit(message,(1100,100))
        pygame.draw.circle(self.screen,self.stones_color[self.othello.turn],(1050,100+int(self.grid_width/2*0.9)),int(self.grid_width/2*0.9))

    def draw_othello(self):
        self.draw_back()
        if self.draw_status.status['marker']:
            self.draw_marker()
        if self.draw_status.status['cursor']:
            self.draw_cursor()
        self.draw_stones()
        self.draw_turn()
    
    def _is_exit(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
    
    def scene_input(self):  
        self.draw_status.init()
        self.othello.add_marker()
        Loop_FIN=False
        while Loop_FIN==False:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    key_dict={K_UP:(-1,0),K_DOWN:(1,0),K_RIGHT:(0,1),K_LEFT:(0,-1)}
                    if event.key==K_SPACE or event.key==K_RETURN:
                        if self.othello.put(self.cursor.position[0],self.cursor.position[1])==0:
                            Loop_FIN=True
                            break
                    elif event.key in key_dict:
                        self.cursor.input_key(key_dict[event.key])
                    else:
                        print('KEYDOWN')
                elif event.type==MOUSEBUTTONDOWN:
                    if self.othello.put(self.cursor.position[0],self.cursor.position[1])==0:
                        Loop_FIN=True
                        break
                elif event.type==MOUSEMOTION:
                    print(event.pos)
            self.draw_status.status['cursor']=True
            self.draw_status.status['marker']=True
            self.draw_othello()
            pygame.display.update()
            # pygame.time.wait(100)
        self.draw_status.init()
        self.othello.erace_marker()
        self.othello.next_turn()
        return 0

    # 石を反転させるシーン
    def scene_reverse(self):
        pass

    # ターンをパスするシーン
    def scene_pass(self):
        pass

    # ゲーム終了シーン
    def scene_gameover(self):
        pass
    
    def run(self):
        while True:
            self.scene_input()
            self._is_exit()
            


def main():
    otGUI=othello_GUI()
    otGUI.run()

def main2():
    otGUI=othello_GUI()
    otGUI.scene_input()


if __name__=='__main__':
    main()