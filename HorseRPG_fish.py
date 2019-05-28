# 題目：https://hackmd.io/soWub2wLT4WeRXtQ0jGxAA

# 為了程式碼裡面不要有一堆if，所以我想使用有 "邊框" 的一維list
# 棋盤的格子若為0， 表示沒有走過，我把棋盤以 n+4 * m+4 的形式表達
# 最外面報上2層-1，以使程式不會跳過去
# 要包兩層而不是一層，是因為馬可以條(2,1)
# n : 棋盤row數量
# m : 棋盤col數量
# x : 起點的col位置
# y : 起點的row位置

def printBoard(board, m):
    for i in range(len(board)):
        if i % (m + 4) == 0 :
            print()
        print(board[i], end = ' ')

def findSol(n, m, x, y) :
    row, col = n+4, m+4
    board = [0 for i in range(row * col)]
    # printBoard(board,m)
    for i in range(0, col) : # 上下四條線填入 -1
        board[i] = -1  
        board[i + col] = -1 
        board[i + col * (n+2)] = -1 
        board[i + col * (n+3)] = -1
    # print('-----ok-----')
    for i in range(0, row) : # 左右四條線填入 -1
        board[i * col] = -1
        board[i * col + 1] = -1
        board[i * col + m + 2] = -1
        board[i * col + m + 3] = -1
    # printBoard(board,m)
    dir = [2*col+1,2*col-1,col+2,col-2,
        -2*col+1,-2*col-1,-col+2,-col-2] # 八個方向的offset
    board[(y+2)*col+x+2] = 1
    return myFindSol(board, dir, n*m, (y+2)*col+x+2, 1)

# board: 棋盤狀況
# dir: 八個方向的offset
# target: 目標要走幾步
# pos: 目前要下的位置
# steps: 要擺第幾個
# foundSols: 傳回值代表找到幾組解
def myFindSol(board, dir, target, pos, steps) :
    global m 
    if target == steps : # 達標了
        # printBoard(board,m)
        return 1
    # board[pos] = steps + 1 # 在預定位置上標示步數
    foundSols = 0
    for i in range(8) : # 八個方向都檢查一下
        if board[pos+dir[i]] == 0: # 可以走
            board[pos+dir[i]] = steps + 1
            foundSols = foundSols + myFindSol(board, dir, target, pos+dir[i], steps+1)
            board[pos+dir[i]] = 0
    board[pos] = 0 # 回報前要清掉自己做過的事
    return foundSols

m = 0

def main() :
    global m
    n, m, x, y = map(int, input().split())
    print(findSol(n, m, x, y))
main()

'''
5,5
9,9
col = 9
row = 9
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 0 0 0 0 0 1 1
1 1 0 0 0 0 0 1 1
1 1 0 0 0 0 0 1 1
1 1 0 0 0 0 0 1 1
1 1 0 0 0 0 0 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
[2*col+1,2*col-1,col+2,col-2,
-2*col+1,-2*col-1,-col+2,-col-2]
【19,17,11,7,
-17,-19,7,-9】
'''