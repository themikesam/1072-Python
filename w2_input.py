# def Main(name):
#     print('Hello, World')
#     print('Hello,', name)
# Main('Old Fish')


# def Main():
#     name = input()
#     print('Hello,', name)
# Main()

# def Main():
#     a = float(input())
#     b = float(input())
#     print('Hello,', a ** b)
# Main()

# def Main():
#     y = float(input())
#     if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):
#         print("1")
#     else:
#         print("2")
# Main()

# def Main():
#     change = int(input())
#     fifty = change // 50
#     change = change % 50
#     ten = change // 10
#     change = change % 10
#     five = change // 5
#     change = change % 5
#     one = change // 1
#     print fifty
#     print ten
#     print five
#     print one
#     # 50
#     # 10
#     # 5
#     # 1
# Main()

import cmath
def Main():
    # 題目
        # ax^2 + bx + c == 0, 求解！
            # a 或 b 或 c 可能是 0
        # -b +- sqrt( b * b - 4ac )
        # --------------------------
        #            2a
    # text = input().split()
    a, b, c = map(float, input().split())
    # a = int(input().split())
    # b = int(input().split())
    # c = int(input().split())
    d = b * b - 4 * a * c 
    # 註解
        # 輸入a,b,c三個float
        # 問ax^2 + bx + c = 0，有哪些解，如
            # 無解: a,b == 0, but c != 0
    if a == 0 and b == 0 and c!= 0 :
        print('no solution!')
            # 無限多解: a,b,c == 0
    elif a == 0 and b == 0 and c == 0:
        print('infinite solution')
            # 一解為x: a = 0, x = -c/b
    elif a == 0:
        print(-c/b)
            # 兩解為x1, x2: see wiki
    else :
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
        print(x1,x2)
Main()


