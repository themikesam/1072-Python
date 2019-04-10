# 學號：104213069
# 姓名：覃融亮
# 作業一
# 題目：https://hackmd.io/PCLLZqSSRlCwuCMGd8tpqg



# 傳入是否閏年，根據傳入的值印出對應的訊息。
def printLeap(ans):
    if ans : print('加薪！！')
    else : print('沒有加薪QQ')

# 傳入年份，判斷是否閏年，是則回傳True，否則回傳False
def isLeap(y):
    # 世紀年皆為平年，僅可被400整除為閏年
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    # 其他：可以被4整除皆為閏年，其餘皆是平年
    else:
        if y % 4 == 0:
            return True
        else:
            return False

printLeap(isLeap(float(input('Please input a year: '))))