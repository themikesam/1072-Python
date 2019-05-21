way = dict()
way = {
        '1' : [-1,-2],
        '2' : [1,-2],
        '3' : [2,-1],
        '4' : [2,1],
        '5' : [1,2],
        '6' : [-1,2],
        '7' : [-2,1],
        '8' : [-2,-1]
    }

# 初始化base大小，二維陣列，預設全部陣列為 -1 , 表示還沒踏過，可以被踏
#   base = [[-1] * row] * col
# 設第一個原點為 0，下一步加 ++，0 > 1 > 2 > 3
#    base[x][y] = 1
# 不能重複踏步，如果下一步不是-1，則continue
# 能回到原點就算一種解

def init(row, col, x, y) :
    base = [[(-1) for i in range(row)] for i in range(col)]
    base[x][y] = 1
    # print(base)
    return myhorse([x,y],1, base)

    
# list 相加
def list_add(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

# list 相減
def list_minus(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]-b[i])
    return c

# 排版輸出
def printcheck(data):
    print('-----')
    for i in range(len(data)):
        for j in range(len(data[i])):
            print("%2d"%data[i][j], end = ' ')
        print()


# pos: 目前x, y軸
# pointer: 目前第幾個n
    # 設第一個原點為 1，下一步加 ++，1 > 2 > 3 ...n
def myhorse(pos, pointer, base):
    # 當pointer達到 row * col 時表示結束
    size = (len(base) * len(base[0]))
    if pointer == size :
    # and -1 not in base:
        # printcheck(base)
        return 1
    count = 0
    way = {
        '1' : [-1,-2],
        '2' : [1,-2],
        '3' : [2,-1],
        '4' : [2,1],
        '5' : [1,2],
        '6' : [-1,2],
        '7' : [-2,1],
        '8' : [-2,-1]
    }
    # for i in range(1,9) : # 每一步都有8種方向，因定義為1...8，因此從1開始到>9結束
    #     nextpos = way[str(i)]
    for i in d:
        nextpos = i
        # nextpos = horse(i)
        pos = list_add(pos,nextpos)

        # 如果任何一點超過邊界
        if(pos[0] >= len(base) or pos[1] >= len(base[0]) or pos[0] < 0 or pos[1] < 0):
            pos = list_minus(pos,nextpos)
            continue

        # 如果nextpos可以被填入值，-1 表示新生兒
        elif(base[pos[0]][pos[1]] == -1):
            pointer += 1
            base[pos[0]][pos[1]] = pointer
            count += myhorse(pos, pointer, base)
            pointer -= 1
            base[pos[0]][pos[1]] = -1
            pos = list_minus(pos,nextpos)
        # 如果nextpos已被填入值
        # else(base[pos[0]][pos[1]] != -1):
        else:
            pos = list_minus(pos,nextpos)
            continue
    return count

    




# 計算馬可以行走的方向
# 如 https://hackmd.io/soWub2wLT4WeRXtQ0jGxAA 圖所示的安排
'''
* 1 * 2 *
8 * * * 3
* * o * *
7 * * * 4
* 6 * 5 *
'''
def horse(n):
    way = {
        1 : [-1,-2],
        2 : [1,-2],
        3 : [2,-1],
        4 : [2,1],
        5 : [1,2],
        6 : [-1,2],
        7 : [-2,1],
        8 : [-2,-1]
    }
    return way.get(n,None)
    

def main():
    data = list(map(int,input().split()))
    print(init(data[0],data[1],data[2],data[3]))

main()