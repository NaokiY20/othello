# 面倒なので、座標系でも表記は統一していない(統一したい)

import numpy
import queue

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
        self.turn_queue=queue.Queue()
        self.turn_queue.put('W')
        self.turn_queue.put('B')

    # ベクトル計算
    def add_vec(self,a,b):
        return list(numpy.array(a)+numpy.array(b))

    def find_red(self):
        for y in range(self.height):
            for x in range(self.width):
                # print(self.search(y,x))
                if self.board[y][x]=='.' and self.search(y,x)!=None:
                    self.board[y][x]='R'
        return

    # explorer関数　-1(False):ひっくり返せるものなし 自然数n:n個ひっくり返せる
    def explorer(self,origin,now_pos,vec):
        # そもそも範囲外の場合
        if not(0<=now_pos[0]<self.height and 0<=now_pos[1]<self.width):
            return -1
        if self.board[now_pos[0]][now_pos[1]]=='.' or self.board[now_pos[0]][now_pos[1]]=='R':
            return -1
        elif self.board[now_pos[0]][now_pos[1]]==origin:
            return 0
        else:
            next_pos=self.add_vec(now_pos,vec)
            res=self.explorer(origin,next_pos,vec)
            if res==-1:
                return -1
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
            if res==-1 or res==0:
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
            self.board[y][x]=self.turn
            self.reverse(y,x)
        return

    # (y,x)を中心に、駒を更新する（反転させる）
    def reverse(self,y,x):
        # それぞれの方向のひっくり返すべき駒の数
        list_rev=self.search(y,x)
        origin_pos=[y,x]
        for i in range(8):
            self.reverser(self.add_vec(origin_pos,self.vec[i]),self.vec[i],list_rev[i])
    
    # reverseの為の再帰関数
    def reverser(self,now_pos,vec,num):
        if num<=0:
            return
        self.board[now_pos[0]][now_pos[1]]=self.turn
        self.reverser(self.add_vec(now_pos,vec),vec,num-1)
        return

    def erase_red(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]=='R':
                    self.board[y][x]='.'
    
    def next_turn(self):
        if self.turn_queue.empty():
            return -1
        next=self.turn_queue.get()
        self.turn=next
        self.turn_queue.put(next)
        
def print_TwoDList(mylists):
    for mylist in mylists:
        for myobj in mylist:
            print(myobj,end=' ')
        print('')
    print('')
    return

def main():
    othello1=othello(8,8)
    print_TwoDList(othello1.board)
    print('')
    othello1.board=[
        ['B','.','.','B','.','.','B','.'],
        ['.','W','.','W','.','W','.','.'],
        ['.','.','W','W','W','.','.','.'],
        ['B','W','W','.','W','W','W','B'],
        ['.','.','W','W','W','.','.','.'],
        ['.','W','.','W','.','B','.','.'],
        ['B','.','.','W','.','.','W','.'],
        ['.','.','.','B','.','.','.','B']]
    print_TwoDList(othello1.board)
    print('')
    othello1.find_red()
    othello1.put(3,3)
    print_TwoDList(othello1.board)
    print('')
    return

def main2():
    ot=othello(8,8)
    print(ot.turn)
    ot.next_turn()
    print(ot.turn)
    ot.next_turn()
    print(ot.turn)
    ot.next_turn()
    print(ot.turn)
    ot.next_turn()
    print(ot.turn)
    ot.next_turn()

if __name__=='__main__':
    main2()