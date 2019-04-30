'''
# n 皇后問題
[i][j] →→→ 請問站住哪三條線？col:列，up：往右上，down：往右下
第一個索引代表row，第二個索引代表col
    1. col[j] →
    2. up[i+j] ↘ ️
    3. down[i-j+n-1] ️↗
'''
def queen(n) :
    return myqueen(n, 0, [True for i in range(n)], [True for i in range(2*n-1)], [True for i in range(2*n-1)])
# n : n 皇后問題
# r : 已經放上r個皇后，負責放r這row
# col : 某col的佔用情況
# up : 往右上斜線的佔用情況
# down: 往右下斜線的佔用情況

def myqueen(n, r, col, up, down) :
    if r == n :
        return 1
    count = 0
    for c in range(n) : # for each col c
        # check if can put on
        # if col[c]==False and up[r+c]==False and down[r-c+n-1]==False:
        # 如果直線和兩條斜線都可以放
        if col[c] and up[r+c] and down[r-c+n-1]:
            # 放上去後這三條線都不能放了
            col[c]=up[r+c]=down[r-c+n-1]=False
            # 移交給下一個皇后
            count += myqueen(n, r+1, col, up, down)
            # 移除皇后後並重設這三條線都可以放
            col[c]=up[r+c]=down[r-c+n-1]=True
    return count

def main():
    print(queen(int(input())))
main()
'''
import random
#冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        #如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

#采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            #产生当前皇后的位置信息
            if len(state) == num-1:
                yield (pos, )
            #否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


#为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

prettyprint(random.choice(list(queens(8))))
'''