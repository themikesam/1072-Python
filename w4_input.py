# # 3 > 10 > 5 > 16 > 8 > 4 > 2 > 1
# # seqlen(3) = 8

# def seqlen(n):
#     num_seq = [n]
#     count = 1
#     # if n < 1:
#         # return count
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#             num_seq.append(n)
#         else:
#             n = 3 * n + 1
#             num_seq.append(n)
#         count += 1
#     print(num_seq)
#     return count


# def Main():
#     print(seqlen(int(input())))
# Main()

# 3 > 10 > 5 > 16 > 8 > 4 > 2 > 1
# seqlen(3) = 8


# --------------------------
# def seqlen(x,y):

#     # 把輸入之兩個數存入num內
#     num = []
#     for i in range(x,y+1):
#         num.append(i)

#     # 把每個num內的值，計算有幾個 3n + 1後，存入num_seq
#     num_seq = []
#     '''
#     print(num)
#     print('共有',len(num),'個數：',num)
#     '''
#     i = 0
#     while i < len(num):
#         count = 1
#         # if num[i] < 1:
#             # return count
#         while num[i] != 1:
#             if num[i] % 2 == 0:
#                 num[i] = num[i] // 2
#             else:
#                 num[i] = 3 * num[i] + 1
#             count += 1
#         num_seq.append(count)
#         i += 1
#     return num_seq


# def Main():
#     while True:
#         try : # try to read 2 int
#             a, b = map(int, input().split())
#             result = seqlen(a,b)
#             # print('每個數的結果',result)
#             # print('最大為',max(result))
#             print(a,b,max(result))
#         except : # if fail, break while loop
#             break
# Main()

# # 3 > 10 > 5 > 16 > 8 > 4 > 2 > 1
# # seqlen(3) = 8

# def seqlen(n):
#     num_seq = [n]
#     count = 1
#     # if n < 1:
#         # return count
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#             num_seq.append(n)
#         else:
#             n = 3 * n + 1
#             num_seq.append(n)
#         count += 1
#     # print(num_seq)
#     return count

# def findMax(x, y):
#     if x > y:
#         x, y = y, x
#     max = 1
#     i = x
#     while i <= y:
#         if seqlen(i) > max:
#             max = seqlen(i)
#         i += 1
#     return max

# def Main():
#     while True:
#         try : # try to read 2 int
#             a, b = map(int, input().split())
#             print(a, b, findMax(a,b))
#         except : # if fail, break while loop
#             break
# Main()


# 123456 -> 654321
# define if x = reverse(x) then we call x is 回文
# give x 
# count = 1
# x = x + reverse
# while x != reverse(x)
#   x = x + reverse(x)
#   count += 1
# while x is not 回文
# show 最後的回文，以及做了幾次加法
# that is print x, count

# input:
# n
# n int
# output:
# add times and palindrome of n
# how to find reverse(x)?
# let result = 0
# while x is not 0
#   append last digit of x to result, %10
#   remove last digit from x, //10
# result will be reverse of x