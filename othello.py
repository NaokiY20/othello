# 面倒なので、座標系でも表記は統一していない(統一したい)

import numpy

class othello():
    def __init__(self,h,w):
        # 全方向の単位ベクトル
        self.vec=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        self.height=h
        self.width=w
        self.board=[]
        for i in range(self.height):
            tmp=[]
            for j in range(self.width):
                tmp.append('.')
            self.board.append(tmp)
        self.board[self.height//2-1][self.width//2-1]='B'
        self.board[self.height//2][self.width//2]='B'
        self.board[self.height//2][self.width//2-1]='W'
        self.board[self.height//2-1][self.width//2]='W'
        self.turn='B'

    # ベクトル計算
    def add_vec(self,a,b):
        return list(numpy.array(a)+numpy.array(b))

    def find_red(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.search(y,x)!=None:
                    self.board[y][x]='R'
        return

    # explorer関数　-1(False):ひっくり返せるものなし 自然数n:n個ひっくり返せる
    def explorer(self,origin,now_pos,vec):
        # そもそも範囲外の場合
        if not(0<=now_pos[0]<self.height and 0<=now_pos[1]<self.width):
            return False
        if self.board[now_pos[0]][now_pos[1]]=='.':
            return False
        elif self.board[now_pos[0]][now_pos[1]]==origin:
            return 0
        else:
            next_pos=self.add_vec(now_pos,vec)
            res=self.explorer(origin,next_pos,vec)
            if res==False:
                return False
            else:
                return res+1

    # (y,x)を中心に、どの方向にいくつひっくり返せるのかを調べる
    def search(self,y,x):
        is_exist=False
        ans=[]
        origin_pos=[y,x]
        origin=self.turn
        for vec in self.vec:
            res=self.explorer(origin,self.add_vec(origin_pos,vec),vec)
            if res==False or res==0:
                ans.append(0)
            else:
                is_exist=True
                ans.append(res)
        if is_exist:
            return ans
        else:
            return None

    # 駒を置く
    def put(self,y,x):
        if self.board[y][x]!='R':
            return -1
        else:
            if self.turn=='B':
                self.board[y][x]='B'
            else:
                self.board[y][x]='W'
        return 0

    # (y,x)を中心に、駒を更新する（反転させる）
    def reverse(self,y,x):
        origin=self.board[y][x]
        for i in range(1,y+1):
            if self.board[y-i][x]=='.':
                break
            if self.board[y-i][x]==origin:
                for j in range(1,i+1):
                    self.board[y-j][x]=origin
        
def print_TwoDList(mylists):
    for mylist in mylists:
        for myobj in mylist:
            print(myobj,end=' ')
        print('')
    return

def main():
    othello1=othello(8,8)
    print_TwoDList(othello1.board)
    othello1.board[0][3]='B'
    othello1.board[1][3]='W'
    othello1.board[2][3]='W'
    othello1.board[3][3]='W'
    othello1.board[4][3]='W'
    othello1.board[5][3]='R'
    othello1.put(5,3)
    print_TwoDList(othello1.board)
    othello1.reverse(5,3)
    print_TwoDList(othello1.board)
    return

if __name__=='__main__':
    main()