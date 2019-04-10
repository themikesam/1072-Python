# 學號：104213069
# 姓名：覃融亮
# 作業五
# 題目：https://hackmd.io/s/S12vSV-OV#

import math
def meanStddev(data) :
    sum = 0 # 累加所分割的「數」後，再處於總個數得平均數
    for x in data : 
        sum = sum + x
    avg = sum / len(data)
    sum = 0 # 對所分割的「數」減平均數平方後累加
    for x in data: 
        sum = sum + (x-avg)*(x-avg)
    dev = math.sqrt(sum/len(data)) # 依據公式處理
    return avg, dev

def splitList(text): # 以空白切割後，轉float再存入list
    data = list()
    words = text.split()
    for word in words:
        data.append(float(word))
    return data

def main():
    # 讀入輸入值後進行切割
    text = input()
    data = splitList(text)
    print('平均值：',meanStddev(data)[0],'，標準差：',meanStddev(data)[1])

main()