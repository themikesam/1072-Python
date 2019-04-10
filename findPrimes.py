# 學號：104213069
# 姓名：覃融亮
# 作業三
# 題目：https://hackmd.io/PCLLZqSSRlCwuCMGd8tpqg

# import time;  # 引入time模块（題目沒要求，但老俞要求，故註解）

def isPrime(n):
    '''
    質數（Prime number），又称素数，指在大於1的自然数中，除了1和該数自身外，無法被其他自然数整除的数
    '''
    i = 2
    # 自然數定義 是 正數不含0，故小於1皆為「非質數」
    if n > 1:
        # 從 2 到 n，若能被整除為因數，不能被整除為質數
        while i < n:
            if n % i == 0:
                return False
            i+=1
        return True
    else:
        return False

def sumPrimes(s,e):
    i = s # 開始值
    sum = 0 # sum用於加總質數
    '''
    從開始值(start)開始計算，
    若是質數，sum加1，
    開始值累加至結束值(end)結束迴圈
    '''
    while i < e:
        i+=1
        if(isPrime(i)): 
            sum+=1
    return sum

def Main():
    # start = time.time() # 程式開始時間（題目沒要求，但老俞要求，故註解）
    s = int(input()) # s : start, 開始數值
    e = int(input()) # e : end, 結束數值
    print('這裡面有',sumPrimes(s,e),'個質數')
    # end = time.time() # 程式結束時間（題目沒要求，但老俞要求，故註解）
    # print('共用了',(end-start),'秒')（題目沒要求，但老俞要求，故註解）

Main()