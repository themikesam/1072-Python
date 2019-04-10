# 學號：104213069
# 姓名：覃融亮
# 作業六
# 題目：https://hackmd.io/s/r1JJe7vu4#

def intFact(myInput):
    ans = []
    if myInput == 1: # 答案
        ans.append(myInput)
    while myInput != 1: # 當輸入值不等於1時，從對輸入值處於質數，
        for i in range(2, int(myInput+1)):
            if myInput % i == 0:  # i是myInput的一個質因數
                ans.append(i)
                myInput = myInput / i # 將myInput除以質因數後繼續分解，直至數值等於1
                break

    # 使用dictionary對於list進行搜尋，相同則累加
    dict = {} 
    for key in ans:
        dict[key] = dict.get(key, 0) + 1
    # 印出現有dictionary中的所有數
    for keys,values in dict.items():
        print(keys,values)

def main():
    intFact(int(input()))

main()