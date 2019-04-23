# a = [[1,2,3],[4,5,6]]
# # [
# #     [1,2,3]
# #     [4,5,6]
# # ]
# print('before',a)
# r = len(a)
# c = len(a[0])
# b = [[a[r-j-1][i] for j in range(r)] for i in range(c)] # 向右旋轉

# # # result
# # [
# #     [4,1]
# #     [5,2]
# #     [6,3]
# # ]
# print('after:right',b)
# c = [[a[j][c-i-1] for j in range(r)] for i in range(c)] # 向左
# [ [ a[j][i] for j in range(r)]for i in range(c)]
# # # result
# # [
# #     [3,6]
# #     [2,5]
# #     [1,4]
# # ]

# print('after:left',c)
# # [[a[r-i-1][c-j-1] for j in range(c)] for i in range(r)] # 
# # # result
# # [
# #     [6,5,4],
# #     [3,2,1]
# # ]

# # flip
# # [[a[r-i-1][j] for j in range(c)] for i in range(r)] # 
# [
#     [
#         a[r-j-1][i] for j in range(r)
#     ] 
#     for i in range(c)
# ]

# # for (i = 0;i < c;i++)
# #     for(j = 0; i < r;j++)
# #         a[r-j-1][i]
def flip(a) :
    r = len(a)
    c = len(a[0])
    return [[a[r-i-1][j] for j in range(c)] for i in range(r)]

def rotate(a) : 
    r = len(a)
    c = len(a[0])
    return [[a[r-j-1][i] for j in range(r)] for i in range(c)]

    

def Main() :
    r, c, m = map(int, input().split())
    ans = [list(map(int,input().split())) for i in range(r)]
    operation = list(map(int,input().split()))

    for val in operation :   
        ans = {
        '1': lambda ans: flip(ans),
        '0': lambda ans: rotate(ans),
        }[str(val)](ans)
    print('-----')
    print(len(ans),len(ans[0]))
    for val in ans :
        output = ''
        for value in val: 
            output += str(value)+' '
        print(output)
Main()