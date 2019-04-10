# 學號：104213069
# 姓名：覃融亮
# 作業二
# 題目：一元二次方程式
# 題目解說：https://hackmd.io/HSWVyBX1RrSmzouf_-1qcg



import cmath
import math
def checkEquation():
    '''
    # 利用' '分割輸入：
    a, b, c = map(float, input().split())
    '''

    # 輸入 a, b, c
    a = float(input())
    b = float(input())
    c = float(input())

    # d = b² - 4ac
    d = b * b - 4 * a * c 

    # 無解: a, b == 0, but c != 0
    if a == 0 and b == 0 and c!= 0 :
        print('no solution!')

    # 無限多解: a, b, c == 0
    elif a == 0 and b == 0 and c == 0:
        print('infinite solution')

    # 一解為x: a = 0, x = -c/b
    elif a == 0:
        print(-c/b)

    # 兩解為x1, x2: see wiki
    else :
        
        # 因題目說明不需顯示虛根，
        # 因此如果 d 為負數，答案需先下絕對值再開根號
        if d < 0:
            x1 = (-b - math.sqrt(abs(d)))/(2*a)
            x2 = (-b + math.sqrt(abs(d)))/(2*a)
        else :
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)

        if d > 0:
            print('兩相異實根')
            print(x1,x2)
        elif d == 0:
            print('兩相同實根(重根)')
            print(x1)
        else :
            print('無解')


checkEquation()