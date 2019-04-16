# 輸入一串數字
# 再輸入一個數字 t
# 請列出總和為t的數字組合
# 1 4 7 28 9 4 2 21 18 32
# 42


# n, 資料有幾筆
# m, 要選幾個
# data, 可以選的list
import time
def comb(data, n, m) :
    mycomb(data, n, m, 0, [])

# valid: valid choice after this position
def mycomb(data, n, m, valid, result) :
    # if m < 0 :
    #     return
    if m == 0 :
        print(result)
        return
    for i in range(valid, n):
        result.append(data[i])
        mycomb(data, n, m - data[i], i + 1, result)
        result.pop()

def main() :
    # start = time.time()
    data = list(map(int,input().split()))
    m = int(input())
    comb(data, len(data), m)
    # end = time.time()
    # print(end-start)
    # print(count)

main()