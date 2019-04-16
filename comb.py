# 組合問題, eg給
# 給ABCDE，已經選了[],再選2個
# --> 有五種可能性
# (1) 給BCDE，已經選了[A]，再選1個
# (2) 給 CDE，已經選了[B]，再選1個
# (3) 給  DE，已經選了[C]，再選1個
# (4) 給   E，已經選了[D]，再選1個
# (5) 給  []，已經選了[E]，再選1個

# n, 資料有幾筆
# m, 要選幾個
# data, 可以選的list
import time
def comb(data, n, m) :
    mycomb(data, n, m, 0, [])

# valid: valid choice after this position
count  =  0
def mycomb(data, n, m, valid, result) :
    if m == 0 :
        print(result)
        return
    for i in range(valid, n):
        result.append(data[i])
        global count
        count += 1
        mycomb(data, n, m - 1, i + 1, result)
        result.pop()

def main() :
    start = time.time()
    data = input().split()
    m = int(input())
    comb(data, len(data), m)
    end = time.time()
    print(end-start)
    print(count)

main()