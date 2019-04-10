# 學號：104213069
# 姓名：覃融亮
# 作業四
# 題目：https://hackmd.io/s/Bks8U7-_E#

def reverse(x):
    x = str(x) # 轉成string
    return int(x[::-1]) # 反向索引後再轉int回傳

def isPalindrome(x):
    count = 0 # 記錄次數
    r = reverse(x) # 翻轉輸入值
    while x != r: # 若不相符則相加，相加後再回文，循環比對，直至相等則回傳次數與最終回文值
        x = int(x) + r
        r = reverse(x)
        count += 1
        if count > 100: # 若次數大於100則直接放棄，別浪費cpu
            return '回合數大於100，可能沒有回文值'
    return count, x

def main():
    n = int(input())
    myInput = list()
    myAnswer = list()

    for i in range(n): # 根據第一次的輸入值迴圈讀取並存入myInput(list)
        myInput.append(input())

    for i in range(n): # 依據儲存好的輸入值運算，運算結果直接存入myAnswer(list)
        myAnswer.append(isPalindrome(myInput[i]))
    
    print('==========')

    for i in myAnswer: # 印出myAnswer(list)所存入的所有內容
        print(i)

main()
