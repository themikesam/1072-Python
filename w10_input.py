# source: https://hackmd.io/OcSeom4QRayidgcUOQDgNQ
# n, 水果有幾種
# money, 有多少錢
# data, 每種水果的價錢
# amount, 要買的數量
import time
def comb(data, n, money, amount) :
    mycomb(data, n, money, amount, 0, [])

# valid: 負責買哪一種水果
def mycomb(data, n, money, amount, valid, result) :
    if amount == 0:
        # print(result)
        output = ''
        for i in range(len(result)):
            if(i==len(result)-1):
                output += result[i]
            else: 
                output += result[i]+'、'
        print(output)
        return
    if valid >= n : # 沒有這種水果啦
        return
    i = 0
    # valid 這樣水果可以買 i 個， 不可超過錢 和 要 買的數量
    while i <= amount and money >= i * data[valid] :
        # result.append(i)
        # result.append({data[valid]:i})
        result.append(str(data[valid])+'元的'+str(i)+'個')
        mycomb(data, n, money - i * data[valid], amount - i, valid + 1, result)
        result.pop()
        i += 1

    # for i in range(valid, n):
    #     result.append(data[i])
    #     mycomb(data, n, m - data[i], i + 1, result)
    #     result.pop()

def main() :
    # data: 每一種水果的價錢
    data = list(map(int,input().split()))
    # 有多少錢
    m = int(input())
    # 要買幾個
    amount = int(input())
    comb(data, len(data), m, amount)

    # end = time.time()
    # print(end-start)
    # print(count)

main()