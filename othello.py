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
        self.turn_dict={'B':'Black','W':'White'}
        self.turn_list=['B','W']
        self.turn_index=0

    # ベクトル計算
    def _add_vec(self,a,b):
        return list(numpy.array(a)+numpy.array(b))

    def _find_marker(self,turn):
        ans=[]
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]=='.' and self._search(y,x,turn)!=None:
                   ans.append([y,x])
        return ans

    def add_marker(self):
        marker_list=self._find_marker(self.turn)
        for mark in marker_list:
            self.board[mark[0]][mark[1]]='R'
        return

    # _explorer関数　-1(False):ひっくり返せるものなし 自然数n:n個ひっくり返せる
    def _explorer(self,origin,now_pos,vec):
        # そもそも範囲外の場合
        if not(0<=now_pos[0]<self.height and 0<=now_pos[1]<self.width):
            return -1
        if self.board[now_pos[0]][now_pos[1]]=='.' or self.board[now_pos[0]][now_pos[1]]=='R':
            return -1
        elif self.board[now_pos[0]][now_pos[1]]==origin:
            return 0
        else:
            next_pos=self._add_vec(now_pos,vec)
            res=self._explorer(origin,next_pos,vec)
            if res==-1:
                return -1
            else:
                return res+1

    # (y,x)を中心に、どの方向にいくつひっくり返せるのかを調べる
    def _search(self,y,x,turn):
        is_exist=False
        ans=[]
        origin_pos=[y,x]
        origin=turn
        for vec in self.vec:
            res=self._explorer(origin,self._add_vec(origin_pos,vec),vec)
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
        list_rev=self._search(y,x,self.turn)
        origin_pos=[y,x]
        for i in range(8):
            self._reverser(self._add_vec(origin_pos,self.vec[i]),self.vec[i],list_rev[i])
    
    # reverseの為の再帰関数
    def _reverser(self,now_pos,vec,num):
        if num<=0:
            return
        self.board[now_pos[0]][now_pos[1]]=self.turn
        self._reverser(self._add_vec(now_pos,vec),vec,num-1)
        return

    def erace_marker(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]=='R':
                    self.board[y][x]='.'
    
    def next_turn(self):
        self.turn_index=(self.turn_index+1)%len(self.turn_list)
        self.turn=self.turn_list[self.turn_index]

    # ゲーム終了判定
    def is_checkmate(self):
        for turn in self.turn_list:
            if len(self._find_marker(turn))>0:
                return False
        return True
    
    def number_of_stone(self):
        ans={}
        for color in self.turn_list:
            ans[color]=0
        for line in self.board:
            for square in line:
                for turn in self.turn_list:
                    if square==turn:
                        ans[turn]+=1
        return ans

    # パスが必要かどうか
    def is_need_pass(self):
        return len(self._find_marker(self.turn))==0
            
        
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
    print('pass',othello1.is_need_pass())
    print('checkmate',othello1.is_checkmate())
    othello1.add_marker()
    othello1.put(3,3)
    print_TwoDList(othello1.board)
    print('pass',othello1.is_need_pass())
    print('checkmate',othello1.is_checkmate())
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
    main()