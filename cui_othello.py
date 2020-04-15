from othello import othello
from config import *
import re

class othello_CUI(othello):
    def print_board(self):
        print('turn:',self.turn_dict[self.turn])
        print('  ',end='')
        for i in range(len(self.board[0])):
            print(i+1,end=' ')
        print('')
        i=0
        for line in self.board:
            print(i+1,end=' ')
            i+=1
            for square in line:
                out='.'
                if square=='R':
                    out='□'
                elif square=='B':
                    out='○'
                elif square=='W':
                    out='●'
                else:
                    out='.'
                print(out,end=' ')
            print('')
        print('')
        return
    # 入力と設置
    def input_othello(self):
        while True:
            self.print_board()
            input_str=input('どこに置きますか？ 「1,1」のように入力してください(横、縦)\n---')
            if input_str=='q' or input_str=='quit':
                return -1
            if re.match(r'\d+,\d+',input_str)==None:
                print('「1,1」のように入力してください(横、縦)')
                continue
            input_pos=list(map(int,re.findall('\d+',input_str)))
            # チェスや将棋にならって入れ替える。(入力は横,縦)(実際のデータは縦、横)
            input_pos[0],input_pos[1]=input_pos[1],input_pos[0]
            input_pos[0]-=1
            input_pos[1]-=1
            if self.put(input_pos[0],input_pos[1])==-1:
                print('そこには置けません')
                continue
            else:
                return 0
    
    def print_result(self):
        print('結果')
        list_stones=self.number_of_stone()
        for color,stone in list_stones.items():
            print(self.turn_dict[color]+':'+str(stone))
            

        

def main():
    ot=othello_CUI(board_height,board_width)
    print('オセロを始めます')
    while True:
        if ot.is_checkmate():
            print('終わりです\n')
            ot.print_result()
        if not ot.is_need_pass():
            ot.add_marker()
            res=ot.input_othello()
            if res==-1:
                print('ゲームを中断します')
                return
            ot.erace_marker()
        ot.next_turn()
    return
    

if __name__=='__main__':
    main()