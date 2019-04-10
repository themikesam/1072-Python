def decompose(n):
    result = list()
    # input int n
    # find 質因數 of n
    i = 2 # 由 i = 2 ~ n 逐一測試能否整除(分解)
    while i <= n :
        count = 0
        while n % i == 0 : # 一直除i，直到不能除
            n = n // i # 除 i
            count += 1 # 次數+1
        if count > 0 : # 如果整除次數 > 0, 則成功的分解
            print(i, count) # 印出因數, 次數
            result.append([i,count])
        i += 1 # 試下一個數字
    return result
def main() :
    n = int(input())
    rel = decompose(n)
    print(rel)
main()