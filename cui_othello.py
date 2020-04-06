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
    def input_othello(self):
        input_str=input('どこに置きますか？ 「1,1」のように入力してください(横、縦)\n---')
        if re.match('\d+,\d+',input_str)==None:
            print('「1,1」のように入力してください(横、縦)')
            return -1
        else:
            ans=list(map(int,re.findall('\d+',input_str)))
            # チェスや将棋にならって入れ替える。(入力は横,縦)(実際のデータは縦、横)
            ans[0],ans[1]=ans[1],ans[0]
            ans[0]-=1
            ans[1]-=1
            if ans[0]>=self.height or ans[1]>=self.width:
                print('入力された数字が大きすぎます')
                return -1
            else:
                return ans
            

        

def main():
    ot=othello_CUI(board_height,board_width)
    print('オセロを始めます')
    while True:
        if ot.is_checkmate():
            print('終わりです\n\n結果')
            each_number=ot.number_of_stone()
            for color,stone in each_number.items():
                print(ot.turn_dict[color]+':'+str(stone))
            break
        if not ot.is_need_pass():
            ot.add_marker()
            # 入力と設置(おそらく一つのメソッドにした方が見やすい)
            while True:
                ot.print_board()
                input_pos=ot.input_othello()
                if input_pos!=-1:
                    if ot.put(input_pos[0],input_pos[1])==-1:
                        print('そこに置けません')
                        continue
                    else:
                        break
            ot.erace_marker()
        ot.next_turn()
    

if __name__=='__main__':
    main()