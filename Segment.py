# 學號：104213069
# 姓名：覃融亮
# 作業七
# 題目：https://hackmd.io/qQ7I5ob7QOClPCTd09DP_g

import sys
def Segment(dataList) :
    # 初始化總計數為0
    sum = 0 
    # 取得系統最大值，作比對用途
    start = sys.maxsize 
    # 最小值
    end = 0 

    # dataList 為已縮排好的list，內容為使用者輸入
    # 與dataList比對，dataList中最小值為start，最大值為end
    for data in dataList : 
        if data[0] < start :
            start = data[0]
        if data[1] > end :
            end = data[1]
    # print('開始',start,'結束',end)

    '''
    設定 flag 陣列，預設為 false，陣列大小為dataList長度，即 end - start
    - 假設dataList內容為 2, 3, 7, 9
    - flag陣列大小為 9 - 2 = 7
    '''
    flag=['false']*(end-start) 

    
    # 計算線段覆蓋長度，迴圈每一筆dataList內容，並把flag設為True已表示覆蓋該線段。
    for i in range(len(dataList)) :
        for j in range(dataList[i][0],dataList[i][1]) :
            flag[j-start] = True

    # 印出flag為True的加總
    print(flag.count(True)) 
def main() :
    # read in data and append to list
    n = int(input())
    segment = list()
    for i in range(n) :
        segment.append(list(map(int,input().split())))
    print(segment)
    # sort the list
    segment.sort()
    # sort the list in list，避免出現交叉輸入，例如應順序輸入，但卻逆序輸入。
    for data in segment :
        data.sort()
    # 呼叫Segment函式進行處理計算
    Segment(segment)
    
main()

# def Segment_fish() :
#     # read in data and append to list
#     n = int(input())
#     segment = list()
#     for i in range(n) :
#         segment.append(list(map(int,input().split())))
#     # sort the list
#     # set sum = 0
#     sum = 0
#     # set start,end = segment[1]
#     # for each segment in   from 2 to n-1
#         # check if overlap with [start,end]
#             # true, then extends[start,end]
#         # else found a new segment
#             # sum [start,end]
#             # set start, end to segment[1]
#     # sum [start,end]
#     # print out sum

# Segment_fish()