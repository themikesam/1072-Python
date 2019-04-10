# 學號：104213069
# 姓名：覃融亮
# 作業八 
# 題目：https://hackmd.io/s/rJwaZH_FN
    
def printSquare(data, n) :
    # 印一下
    for i in range(n) :
        for j in range(n) :
            print('{: 03}'.format(data[i][j]), end = '')
        print()
def square(n, data) :
    # 設定 row 跟 col 的初始值(要填的第一個數字的位置)
    # 初始值即是 第一個 row 的正中間，在該位置填入 1
    row = 0
    col = n // 2
    data[row][col] = 1
    # 依序填入 2 ~ n * n
    for num in range(2, n * n + 1) :
        # 從起始點位置開始往右上方填入
        # 如果超過邊界就跳到另一邊
        nextPos = data[(row - 1) % n][(col + 1) % n]
        # 如果要填入數字的地方已經有數字
        if nextPos != 0 :
            # 回到當前數字的正下方
            data[(row + 1) % n][col] = num
            row = (row + 1) % n
        # else
        else :
            # 填入數字
            data[(row - 1) % n][(col + 1) % n] = num
            # row col 變成當前位置
            row = (row - 1) % n
            col = (col + 1) % n
        # 呼叫函數印出方陣
    printSquare(data,n)

def main() :
    # 輸入 n 表示要建立的魔方陣大小
    n = int(input())
    # 建立 n * n 大小的二維陣列
    data = [[0 for i in range(n)] for j in range(n)]
    # 呼叫函數填入數字
    square(n, data)
main()