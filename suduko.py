# [數獨](https://zh.wikipedia.org/zh-tw/%E6%95%B8%E7%8D%A8)
# 測試資料：
# 6 0 9 0 0 0 7 0 4 0 0 0 9 0 0 6 3 0 0 0 0 0 7 0 0 8 9 5 4 0 0 9 6 0 7 3 0 0 0 0 3 0 0 0 0 9 3 0 4 1 0 0 6 5 3 6 0 0 8 0 0 0 0 0 7 2 0 0 4 0 0 0 8 0 4 0 0 0 3 0 6
# 有9條直線、9條橫線、9個區塊 (81格)
# 對點(x,y)而言，他屬於直線[y]，橫線[x]，區塊[x//3*3  + y//3]
# 有9種數字，同數字互斥，不同數字不互斥，所以上面有9種
# 有81個字要填，如果已經確定的，填下一個，否則嘗試所有可能的
# 目標：填入81個數字，一開始已填入0個
# 因此函數的參數應該有（盤面、已填、直線、橫線、區塊）
# 盤面我打算用一維list

def unique(盤面) : 
    直線 = [[True for j in range(9)] for i in range(9)]
    橫線 = [[True for j in range(9)] for i in range(9)]
    區塊 = [[True for j in range(9)] for i in range(9)]
    # 由已經確認的數字，消掉
    for i in range(81) :
        if 盤面[i] != 0 : # 非0表示數字已確定
            x = i // 9 # row
            y = i % 9 # col
            直線[y][盤面[i] - 1] = 橫線[x][盤面[i] - 1] = 區塊[x//3*3 + y//3][盤面[i] - 1] = False
    myunique(盤面, 0, 直線, 橫線, 區塊)

def myunique(盤面, 已填, 直線, 橫線, 區塊) :
    if 已填 == 81:
        for i in range(9) :
            for j in range(9) :
                print(盤面[i*9+j], end = ' ')
            print()
        # print(盤面)
        return
    if 盤面[已填] != 0 :
        myunique(盤面, 已填 + 1, 直線, 橫線, 區塊)
    else :
        x = 已填 // 9
        y = 已填 % 9
        for i in range(9) : # 看看每一個數字能不能填
            if 直線[y][i] and 橫線[x][i] and 區塊[x//3*3 + y//3][i] :
                盤面[已填] = i + 1
                直線[y][i] = 橫線[x][i] = 區塊[x//3*3 + y//3][i] = False
                myunique(盤面, 已填 + 1, 直線, 橫線, 區塊)
                盤面[已填] = 0
                直線[y][i] = 橫線[x][i] = 區塊[x//3*3 + y//3][i] = True



def main() :
    盤面 = list(map(int,input().split()))
    unique(盤面)
main()