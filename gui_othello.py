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
    
    def input_key(self,pressed_key):
        is_pressed=False
        if pressed_key[K_LEFT]:
            self.position[1]+=-1
            is_pressed=True
        if pressed_key[K_RIGHT]:
            self.position[1]+=1
            is_pressed=True
        if pressed_key[K_UP]:
            self.position[0]+=-1
            is_pressed=True
        if pressed_key[K_DOWN]:
            self.position[0]+=1
            is_pressed=True
        self.position[0]%=config.height_num
        self.position[1]%=config.width_num
        if is_pressed:
            pygame.time.wait(config.cursor_speed)   

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

        self.draw_status={'marker':False,'cursor':False,'mes_unputable':False}
        self.cursor=cursor()
        

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

    def draw_othello(self):
        self.draw_back()
        if self.draw_status['marker']:
            self.draw_marker()
        if self.draw_status['cursor']:
            self.draw_cursor()
        self.draw_stones()
    
    def _is_exit(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()


    # プレイヤーからの入力待ち
    def scene_input(self):
        while True:
            pressed_key=pygame.key.get_pressed()
            self.cursor.input_key(pressed_key)
            if pressed_key[K_RETURN]:
                pygame.time.wait(500)
                print(self.cursor.position)
                res=self.othello.put(self.cursor.position[0],self.cursor.position[0])
                print(res)
                if res==0:
                    print("success")
                    self.draw_status['mes_unputable']=False
                    return 0
                else:
                    print("false")
                    self.draw_status['mes_unputable']=True
            
            self.draw_status['cursor']=True
            self.draw_status['marker']=True
            self.draw_othello()

            # pygame.time.wait(config.fps)
            pygame.display.update()
            self._is_exit()

    # 石を反転させるシーン
    def scene_reverse(self):
        pass

    # ターンをパスするシーン
    def scene_pass(self):
        pass

    # ターンを開始するシーン(今は実装の予定なし)
    def scene_start_turn(self):
        pass

    # ゲーム終了シーン
    def scene_gameover(self):
        pass
    
    def run(self):
        while True:
            print(self.othello.turn)
            self.othello.add_marker()
            self.scene_input()
            pygame.time.wait(100)
            self.othello.erace_marker()
            self.othello.next_turn()
            self._is_exit()
            


def main():
    otGUI=othello_GUI()
    otGUI.run()


if __name__=='__main__':
    main()