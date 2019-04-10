# # input 3 int，代表三角形的三個邊
# # output : 
# # case (1) 不是三角形
# # case (2) 直腰三角形
# # case (3) 等腰三角形
# # case (4) 三角形

# def Triangle() :
#     '''
#            a
#           /\ 
#       ab /  \ ca
#         /    \
#       b ￣￣￣￣  c
#           bc
#     '''
#     # side ab
#     ab = int(input())
#     # side bc
#     bc = int(input())
#     # side ca
#     ca = int(input())
#     # 計算任兩邊之和
#     length_CA = ab + bc
#     length_BC = ab + ca
#     length_AB = bc + ca
#     # 任兩邊大於第三邊
#     # print(length_CA > ca and length_BC > bc and length_AB > ab) 
#     if (length_CA > ca and length_BC > bc and length_AB > ab) :
#         if ab == bc == ca :
#             print('等腰三角形')
#         elif ab == bc or bc == ca or ab == ca :
#             print('直角三角形')
#         else :
#             print('三角形')
#     else :
#         print('不是三角形')

# def Triangle_ans():
#     '''
#           /\ 
#       a  /  \ c
#         /    \
#         ￣￣￣￣  
#           b
#     '''
#     a = input()
#     b = input()
#     c = input()
#     if a+b<=c or b+c<=a or a+c<=b:
#         print('不是三角形')
#     elif a==b or b==c or a==c:
#         print('等腰三角形')
#     elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print('直角三角形')
#     else :
#         print('三角形')

# Triangle()
# Triangle_ans()






def Main():
    n = int(input())
    i = 0
    while i < n:
        
        # print(i)
        # # print ith line, has n '*'
        # print(n*'*')

        # # print like this
        # # *
        # # **
        # # ***
        # # ****
        # print(i * '*')

        # # print like this
        # # print ith line, has n-i ' ' + i * ’*‘
        # #    *
        # #   **
        # #  ***
        # # ****
        # i = i + 1
        # print((n-i)*'?'+i*'*')

        # print like this
        # print ith line, has n-i ' ' + i * ’*‘
        #    *
        #   ***
        #  *****
        # *******
        i = i + 1
        print(' '*(n-i) + (i*2-1)*'*')

    while i > 0:
        #  *****
        #   ***
        #    *
        i = i - 1
        print(' '*(n-i) + (i*2-1)*'*')
        
Main()