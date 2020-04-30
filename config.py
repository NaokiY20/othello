
height_num=8
width_num=8

# GUI
window_large=(1280,720)
title="オセロ-othello-"
fps=30

# 色
back_green=(0,128,0)
line_color=(0,0,0)
black_color=(0,0,0)
white_color=(255,255,255)
marker_color=(255,150,150)
cursor_color=(255,255,128)

GUIboard_origin=[5,5]
# GUIboard_height=700
# GUIboard_width=700
line_thick=2

grid_height=80
grid_width=80

# 連続押しのdelayとinterval
cursor_delay=500
cursor_interval=50

# 画面の大きさ　1.0:1280x720
magnification=1.0
def resize(value):
    if(type(value)==tuple):
        tmp=list(value)
        ans=[]
        for i in tmp:
            ans.append(int(i*magnification))
        return tuple(ans)
    if(type(value)==list):
        ans=[]
        for i in value:
            ans.append(int(i*magnification))
        return ans
    else:
        return int(value*magnification)

window_large=resize(window_large)
line_thick=resize(line_thick)
grid_height=resize(grid_height)
grid_width=resize(grid_width)